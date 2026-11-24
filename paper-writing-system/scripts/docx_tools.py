#!/usr/bin/env python3
"""docx 读取与最小替换工具（仅用标准库）。

用法：
  python docx_tools.py text   稿件.docx [--json]          导出正文、脚注、表格单元格文本
  python docx_tools.py replace 原稿.docx 新稿.docx 替换表.tsv  按"旧文本<TAB>新文本"逐行做最小替换

替换规则：旧文本必须在文档 XML 中恰好出现一次（位于同一个文本块内）；
找不到或出现多次的行不替换，并在输出里列出，交由人工处理。原稿不被修改。
"""
import sys, re, json, zipfile, shutil, os

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = re.compile(r'<w:p[ >](?:(?!<w:p[ >]).)*?</w:p>', re.S)
TEXT = re.compile(r'<w:t(?: [^>]*)?>([^<]*)</w:t>|<w:tab/>|<w:noBreakHyphen/>|<w:footnoteReference [^>]*/>')


def _unesc(s):
    return s.replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&apos;', "'").replace('&amp;', '&')


def para_text(xml):
    out = []
    for m in TEXT.finditer(xml):
        s = m.group(0)
        if s.startswith('<w:tab'):
            out.append('\t')
        elif s.startswith('<w:noBreakHyphen'):
            out.append('-')
        elif s.startswith('<w:footnoteReference'):
            out.append('{FN}')
        else:
            out.append(_unesc(m.group(1)))
    return ''.join(out)


def read(path):
    """返回 [{'part': 'body'|'footnote', 'i': 序号, 'in_table': bool, 'text': ...}]"""
    z = zipfile.ZipFile(path)
    items = []
    body = z.read('word/document.xml').decode('utf8')
    # 标出表格范围
    tables = [(m.start(), m.end()) for m in re.finditer(r'<w:tbl>.*?</w:tbl>', body, re.S)]
    for i, m in enumerate(PARA.finditer(body)):
        in_tbl = any(a <= m.start() < b for a, b in tables)
        items.append({'part': 'body', 'i': i, 'in_table': in_tbl, 'text': para_text(m.group(0))})
    if 'word/footnotes.xml' in z.namelist():
        fx = z.read('word/footnotes.xml').decode('utf8')
        for i, m in enumerate(PARA.finditer(fx)):
            t = para_text(m.group(0)).strip()
            if t:
                items.append({'part': 'footnote', 'i': i, 'in_table': False, 'text': t})
    return items


def replace(src, dst, pairs):
    if os.path.abspath(src) == os.path.abspath(dst):
        raise SystemExit('新稿文件名不能与原稿相同')
    z = zipfile.ZipFile(src)
    parts = {n: z.read(n) for n in z.namelist()}
    targets = ['word/document.xml', 'word/footnotes.xml']
    xml = {n: parts[n].decode('utf8') for n in targets if n in parts}
    done, failed = [], []
    for old, new in pairs:
        o = old.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        n = new.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        hits = sum(x.count(o) for x in xml.values())
        if hits != 1:
            failed.append((old, hits))
            continue
        for k in xml:
            if o in xml[k]:
                xml[k] = xml[k].replace(o, n)
        done.append(old)
    for k, v in xml.items():
        parts[k] = v.encode('utf8')
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as out:
        for n in z.namelist():
            out.writestr(z.getinfo(n), parts[n])
    return done, failed


def main():
    if len(sys.argv) < 3:
        print(__doc__); return
    cmd = sys.argv[1]
    if cmd == 'text':
        items = read(sys.argv[2])
        if '--json' in sys.argv:
            print(json.dumps(items, ensure_ascii=False, indent=1))
        else:
            for it in items:
                if it['text'].strip():
                    tag = 'FN' if it['part'] == 'footnote' else ('TB' if it['in_table'] else 'P')
                    print(f"[{tag}{it['i']}] {it['text']}")
    elif cmd == 'replace':
        src, dst, tsv = sys.argv[2:5]
        pairs = []
        for line in open(tsv, encoding='utf8'):
            line = line.rstrip('\n')
            if line and '\t' in line and not line.startswith('#'):
                a, b = line.split('\t', 1); pairs.append((a, b))
        done, failed = replace(src, dst, pairs)
        print(f'已替换 {len(done)} 处，未替换 {len(failed)} 处')
        for old, hits in failed:
            print(f'  未替换（出现 {hits} 次）：{old[:60]}')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
