#!/usr/bin/env python3
"""Word 排版插件：按排版档案检查或统一 docx 格式。

用法：
  python docx_format.py check  稿件.docx --profile cn-workingpaper [--out 报告.md]
  python docx_format.py apply  稿件.docx 新稿.docx --profile cn-workingpaper

check 只报告偏差，不改文件；apply 输出新文件，原稿不动。
段落类别靠文本特征识别（标题编号、"摘要："、"表 N"、参考文献区等），不依赖 Word 样式，
因此对作者手工排版的初稿同样适用。识别不了的段落按正文处理，结果在报告中列出供核对。
依赖：python-docx、lxml。
"""
import sys, os, re, json, argparse, collections
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
ALIGN = {'left': WD_ALIGN_PARAGRAPH.LEFT, 'center': WD_ALIGN_PARAGRAPH.CENTER,
         'justify': WD_ALIGN_PARAGRAPH.JUSTIFY, 'right': WD_ALIGN_PARAGRAPH.RIGHT}
ALIGN_R = {v: k for k, v in ALIGN.items()}


def load_profile(name):
    p = name if name.endswith('.json') else os.path.join(HERE, 'profiles', name + '.json')
    return json.load(open(p, encoding='utf8'))


def body_blocks(doc):
    """按文档顺序返回 ('p', Paragraph) 或 ('tbl', Table)。"""
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    out = []
    for el in doc.element.body.iterchildren():
        if el.tag == qn('w:p'):
            out.append(('p', Paragraph(el, doc)))
        elif el.tag == qn('w:tbl'):
            out.append(('tbl', Table(el, doc)))
    return out


def has_drawing(p):
    return bool(p._p.xpath('.//w:drawing') or p._p.xpath('.//w:pict'))


def has_math(p):
    return bool(p._p.xpath('.//*[local-name()="oMath"]'))


def classify(blocks):
    """返回与 blocks 对齐的类别列表（表格为 None）。"""
    cls = []
    seen_text = False
    in_refs = False
    prev_kind = None
    for kind, b in blocks:
        if kind == 'tbl':
            cls.append(None); prev_kind = 'tbl'; in_refs = False; continue
        t = b.text.strip()
        c = None
        if not t:
            c = 'empty'
        elif has_math(b) or re.fullmatch(r'[（(]\s*\d+\s*[)）]', t):
            c = 'equation'
        elif not seen_text:
            c = 'title'
        elif re.match(r'^(摘\s*要|Abstract)\s*[:：.]?', t):
            c = 'abstract'
        elif re.match(r'^(关键词|关 键 词|Key\s*words|JEL)', t, re.I):
            c = 'keywords'
        elif re.fullmatch(r'(参考文献|References|REFERENCES)', t):
            c = 'refs_heading'; in_refs = True
        elif re.match(r'^(附录|Appendix)\b', t) and len(t) < 50:
            c = 'refs_heading'; in_refs = False
        elif re.match(r'^\d+\.\d+\.\d+\s+\S', t) and len(t) < 60:
            c = 'h3'
        elif re.match(r'^\d+\.\d+\s+\S', t) and len(t) < 60:
            c = 'h2'
        elif (re.match(r'^\d+\.\s*\S', t) or re.match(r'^[一二三四五六七八九十]+、', t)) and len(t) < 50 and not t.endswith('。'):
            c = 'h1'; in_refs = False
        elif re.match(r'^Panel\s+[A-Z]\b', t) and len(t) < 80:
            c = 'panel'
        elif re.match(r'^\[?此处插入', t) or re.match(r'^\[(Insert|INSERT)', t):
            c = 'placeholder'; in_refs = False
        elif re.match(r'^(附表|表|图|Table|Figure)\s*[A-Z]?\d+(\s|$)', t) and len(t) < 90 and '。' not in t:
            c = 'caption'; in_refs = False
        elif in_refs and not has_drawing(b):
            c = 'reference'
        elif prev_kind in ('tbl', 'drawing', 'caption') or re.match(r'^(注|资料来源|数据来源|Notes?)\s*[:：.]', t) or re.match(r'^本(表|图)', t):
            c = 'note'
        else:
            c = 'body'
        if t: seen_text = True
        cls.append(c)
        prev_kind = 'drawing' if (kind == 'p' and has_drawing(b)) else (prev_kind if c in ('empty',) else c)
    return cls



RPR_ORDER = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike', 'outline', 'shadow', 'emboss', 'imprint',
             'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing', 'w', 'kern', 'position', 'sz', 'szCs', 'highlight', 'u',
             'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang', 'eastAsianLayout', 'specVanish', 'oMath']
TCPR_ORDER = ['cnfStyle', 'tcW', 'gridSpan', 'hMerge', 'vMerge', 'tcBorders', 'shd', 'noWrap', 'tcMar', 'textDirection', 'tcFitText', 'vAlign', 'hideMark']


def insert_ordered(parent, child, order, ns):
    """按 OOXML 架构顺序插入子元素。"""
    name = child.tag.split('}')[1]
    idx = order.index(name)
    for i, el in enumerate(parent):
        tag = el.tag.split('}')[1] if '}' in el.tag else el.tag
        if tag in order and order.index(tag) > idx:
            parent.insert(i, child); return child
    parent.append(child); return child

# ---------- 读取当前格式 ----------
def first_run(p):
    return next((r for r in p.runs if r.text.strip()), None)


def run_east(r):
    rpr = r._r.rPr
    if rpr is not None and rpr.rFonts is not None:
        return rpr.rFonts.get(qn('w:eastAsia'))
    return None


def current(p, skip_label=False):
    r = first_run(p)
    if skip_label:
        r = next((x for x in p.runs if x.text.strip() and not re.match(r'^\s*(摘\s*要|关键词|关 键 词|Abstract|Key\s*words|JEL)?\s*[：:]?\s*$', x.text)), r)
    pf = p.paragraph_format
    return dict(
        east=run_east(r) if r else None, latin=r.font.name if r else None,
        size=r.font.size.pt if r and r.font.size else None, bold=bool(r.bold) if r else None,
        align=ALIGN_R.get(p.alignment), line=pf.line_spacing if isinstance(pf.line_spacing, float) else None)


# ---------- 写格式 ----------
def set_run(r, latin, east, size, bold=None, italic=None):
    r.font.name = latin
    rpr = r._r.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = insert_ordered(rpr, OxmlElement('w:rFonts'), RPR_ORDER, None)
    for k in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rf.set(qn(k), latin)
    rf.set(qn('w:eastAsia'), east)
    for k in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(k)) is not None: del rf.attrib[qn(k)]
    if size: r.font.size = Pt(size)
    if bold is not None: r.bold = bold
    if italic is not None: r.italic = italic


def set_indent_chars(p, chars, size):
    pf = p.paragraph_format
    pf.first_line_indent = Pt(chars * size) if chars else Pt(0)
    ind = p._p.get_or_add_pPr().find(qn('w:ind'))
    if ind is not None:
        if chars: ind.set(qn('w:firstLineChars'), str(int(chars * 100)))
        else:
            for k in ('w:firstLineChars', 'w:hangingChars'):
                if ind.get(qn(k)) is not None: del ind.attrib[qn(k)]


def apply_para(p, spec, latin):
    pf = p.paragraph_format
    if 'align' in spec: p.alignment = ALIGN[spec['align']]
    if 'line' in spec: pf.line_spacing = spec['line']
    if 'before' in spec: pf.space_before = Pt(spec['before'])
    if 'after' in spec: pf.space_after = Pt(spec['after'])
    if 'hanging_cm' in spec:
        pf.left_indent = Cm(spec['hanging_cm']); pf.first_line_indent = Cm(-spec['hanging_cm'])
    elif 'indent_cm' in spec:
        pf.first_line_indent = Cm(spec['indent_cm'])
    elif 'indent_chars' in spec:
        set_indent_chars(p, spec['indent_chars'], spec.get('size', 12))
    label_done = False
    for r in p.runs:
        is_label = False
        if 'label_bold' in spec and not label_done:
            if re.match(r'^\s*(摘\s*要|关键词|关 键 词|Abstract|Key\s*words|JEL)', r.text, re.I) or (r.text.strip() in ('：', ':')):
                is_label = True
            elif r.text.strip():
                label_done = True
        if is_label:
            set_run(r, latin, spec.get('label_east', spec['east']), spec.get('size'), spec.get('label_bold', True))
        else:
            set_run(r, latin, spec['east'], spec.get('size'), spec.get('bold'), spec.get('italic'))


def set_cell_borders(cell, top=None, bottom=None):
    tcPr = cell._tc.get_or_add_tcPr()
    b = tcPr.find(qn('w:tcBorders'))
    if b is None:
        b = insert_ordered(tcPr, OxmlElement('w:tcBorders'), TCPR_ORDER, None)
    for el in list(b): b.remove(el)
    vals = {'top': top, 'bottom': bottom}
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{side}'); sz = vals.get(side)
        if sz:
            e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), str(sz)); e.set(qn('w:space'), '0'); e.set(qn('w:color'), '000000')
        else:
            e.set(qn('w:val'), 'nil')
        b.append(e)


def header_rows(tbl):
    n = 0
    for row in tbl.rows:
        txt = ' '.join(c.text for c in row.cells[1:])
        if re.search(r'-?\d+\.\d{2,}', txt): break
        n += 1
    return max(1, min(n, 3))


def apply_table(tbl, prof):
    spec = prof['classes']['table_cell']; latin = prof['latin_font']; t = prof['table']
    rows = tbl.rows; h = header_rows(tbl)
    for i, row in enumerate(rows):
        for j, cell in enumerate(row.cells):
            top = t['top_sz'] if i == 0 else None
            bottom = t['header_sz'] if i == h - 1 else (t['bottom_sz'] if i == len(rows) - 1 else None)
            if t.get('style') == 'three-line': set_cell_borders(cell, top, bottom)
            for p in cell.paragraphs:
                p.alignment = ALIGN[spec.get('first_col_align', spec['align'])] if j == 0 else ALIGN[spec['align']]
                p.paragraph_format.line_spacing = spec['line']
                p.paragraph_format.first_line_indent = Pt(0)
                for r in p.runs: set_run(r, latin, spec['east'], spec['size'])


def apply_footnotes(doc, prof):
    spec = prof['classes']['footnote']; latin = prof['latin_font']; n = 0
    for rel in doc.part.rels.values():
        if rel.reltype.endswith('/footnotes'):
            part = rel.target_part
            from lxml import etree
            root = etree.fromstring(part.blob)
            W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
            for r in root.iter(f'{{{W}}}r'):
                rpr = r.find(f'{{{W}}}rPr')
                if rpr is None:
                    rpr = etree.Element(f'{{{W}}}rPr'); r.insert(0, rpr)
                rf = rpr.find(f'{{{W}}}rFonts')
                if rf is None:
                    rf = insert_ordered(rpr, etree.Element(f'{{{W}}}rFonts'), RPR_ORDER, W)
                for k in ('ascii', 'hAnsi', 'cs'): rf.set(f'{{{W}}}{k}', latin)
                rf.set(f'{{{W}}}eastAsia', spec['east'])
                for tag in ('sz', 'szCs'):
                    e = rpr.find(f'{{{W}}}{tag}')
                    if e is None: e = insert_ordered(rpr, etree.Element(f'{{{W}}}{tag}'), RPR_ORDER, W)
                    e.set(f'{{{W}}}val', str(int(spec['size'] * 2)))
                n += 1
            part._blob = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
    return n


def apply_page(doc, pg):
    for s in doc.sections:
        s.page_width, s.page_height = Cm(pg['width_cm']), Cm(pg['height_cm'])
        s.top_margin, s.bottom_margin = Cm(pg['top_cm']), Cm(pg['bottom_cm'])
        s.left_margin, s.right_margin = Cm(pg['left_cm']), Cm(pg['right_cm'])


def check(path, prof):
    doc = docx.Document(path); blocks = body_blocks(doc); cls = classify(blocks)
    lines = [f'# 排版检查：{os.path.basename(path)}（档案 {prof["name"]}）', '']
    s = doc.sections[0]; pg = prof['page']
    dev_pg = [k for k, v in (('top_cm', s.top_margin.cm), ('bottom_cm', s.bottom_margin.cm), ('left_cm', s.left_margin.cm), ('right_cm', s.right_margin.cm), ('width_cm', s.page_width.cm)) if abs(v - pg[k]) > 0.05]
    lines.append(f'- 页面：{"符合" if not dev_pg else "偏差 " + ", ".join(dev_pg)}')
    cnt = collections.Counter(c for c in cls if c and c != 'empty')
    lines.append(f'- 段落识别：{dict(cnt)}'); lines.append('')
    dev = collections.defaultdict(list)
    for (kind, b), c in zip(blocks, cls):
        if kind != 'p' or c in (None, 'empty', 'equation'): continue
        spec = prof['classes'].get(c); cur = current(b, c in ('abstract', 'keywords'))
        if not spec or cur['size'] is None: continue
        diffs = []
        if cur['east'] and cur['east'] != spec['east']: diffs.append(f"中文字体 {cur['east']}→{spec['east']}")
        if cur['latin'] and cur['latin'] != prof['latin_font']: diffs.append(f"西文字体 {cur['latin']}→{prof['latin_font']}")
        if abs(cur['size'] - spec['size']) > 0.1: diffs.append(f"字号 {cur['size']}→{spec['size']}")
        if 'bold' in spec and c not in ('abstract', 'keywords') and cur['bold'] != spec['bold']: diffs.append(f"加粗 {cur['bold']}→{spec['bold']}")
        if 'align' in spec and cur['align'] and cur['align'] != spec['align']: diffs.append(f"对齐 {cur['align']}→{spec['align']}")
        if 'line' in spec and cur['line'] and abs(cur['line'] - spec['line']) > 0.1: diffs.append(f"行距 {cur['line']:.2f}→{spec['line']}")
        if diffs: dev[c].append((b.text.strip()[:30], '；'.join(diffs)))
    if not dev: lines.append('- 段落格式：全部符合。')
    for c, lst in dev.items():
        lines.append(f'- **{c}** 偏差 {len(lst)} 段')
        for t, d in lst[:6]: lines.append(f'  - 「{t}」 {d}')
    ntab = sum(1 for k, _ in blocks if k == 'tbl')
    lines.append(f'- 表格 {ntab} 张（apply 时统一为三线表、单元格 {prof["classes"]["table_cell"]["size"]} 磅）。')
    unknown = [b.text.strip()[:30] for (k, b), c in zip(blocks, cls) if k == 'p' and c == 'body' and len(b.text.strip()) < 25]
    if unknown: lines.append(f'- 识别为正文的短段落（请核对是否应为标题或图注）：{unknown[:10]}')
    return '\n'.join(lines) + '\n'


def apply(src, dst, prof):
    if os.path.abspath(src) == os.path.abspath(dst): raise SystemExit('新稿文件名不能与原稿相同')
    doc = docx.Document(src); blocks = body_blocks(doc); cls = classify(blocks)
    apply_page(doc, prof['page']); latin = prof['latin_font']; n = collections.Counter()
    for (kind, b), c in zip(blocks, cls):
        if kind == 'tbl':
            apply_table(b, prof); n['table'] += 1; continue
        if c in ('empty', 'equation') or c not in prof['classes']: continue
        apply_para(b, prof['classes'][c], latin); n[c] += 1
    n['footnote_runs'] = apply_footnotes(doc, prof)
    doc.save(dst)
    return n


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['check', 'apply']); ap.add_argument('src'); ap.add_argument('dst', nargs='?')
    ap.add_argument('--profile', default='cn-workingpaper'); ap.add_argument('--out')
    a = ap.parse_args(); prof = load_profile(a.profile)
    if a.cmd == 'check':
        rep = check(a.src, prof)
        if a.out: open(a.out, 'w', encoding='utf8').write(rep); print('写入', a.out)
        else: print(rep)
    else:
        if not a.dst: raise SystemExit('apply 需要输出文件名')
        n = apply(a.src, a.dst, prof); print('已排版：', dict(n), '→', a.dst)


if __name__ == '__main__':
    main()
