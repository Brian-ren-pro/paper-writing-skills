#!/usr/bin/env python3
"""一键检查：语言红线、冒号、节首节末、长句、人称、术语、交叉引用、数字、参考文献。

用法：
  python run_checks.py 稿件.docx --mode ZE|ZC|E [--terms work/terms.md] [--facts work/facts.csv] [--out work/check-report.md]

只读不改。输出 Markdown 报告，每个命中项给出位置（P 正文段号 / FN 脚注 / TB 表格）与原句。
规则依据：language/zh.md §A §B §C §E §F §I、language/en.md、structure.md §5、sections/results.md §6、language/ai-tone.md。
terms.md 格式：每行"标准名 | 别名1, 别名2"（别名为应被统一掉的写法）。
"""
import sys, re, csv, argparse, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_tools import read

CJK = re.compile(r'[一-鿿]')
HEAD = re.compile(r'^(\d+(?:\.\d+){0,3})\.?\s+\S')


def sents_zh(t):
    return [s for s in re.split(r'(?<=[。！？])', t) if s.strip()]


def sents_en(t):
    t2 = re.sub(r'\b(et al|e\.g|i\.e|cf|vs|Fig|No|Eq|U\.S)\.', lambda m: m.group(0).replace('.', '§'), t)
    return [s.replace('§', '.') for s in re.split(r'(?<=[.?!])\s+(?=[A-Z(“"])', t2) if s.strip()]


def loc(it):
    return ('FN' if it['part'] == 'footnote' else 'TB' if it['in_table'] else 'P') + str(it['i'])


ZH_RED = [
    ('不是……而是', r'不是[^。；\n]{0,30}而是'), ('没有……而是', r'没有[^。；\n]{0,30}而是'),
    ('需要说明的是', r'需要说明的是'), ('值得注意的是', r'值得注意的是'), ('诚然', r'诚然'), ('退一步讲', r'退一步(讲|说)'),
    ('边界条件', r'边界条件'), ('截面', r'(?<!横)截面|横截面'), ('指向（结论动词）', r'指向'),
    ('证明/充分说明', r'证明了|充分说明'), ('首次/第一篇/填补空白（须过事实门）', r'首次(发现|研究|考察|提出)|第一篇|填补[^。]{0,6}空白'),
    ('宣布式过渡', r'同样的逻辑(延伸|适用)'), ('"与……一致"收束（技术性比对除外）', r'这一(模式|结果|关系)[^。]{0,20}一致|与[^。，]{0,15}(分析|解释|预测|假说)[^。，]{0,6}一致'),
]
EN_RED = [
    ('banned words', r'\b(delve|landscape|realm|intricate|tapestry|pivotal|underscores?|nuanced)\b|It is worth noting|Interestingly,'),
    ('novel (self)', r'\b(our|this) (paper|study)[^.]{0,30}\bnovel\b|\bnovel (dataset|approach|evidence)\b'),
    ('"not only statistically"', r'not only statistically'), ('"In recent years ... attention"', r'In recent years,[^.]{0,80}attention'),
    ('first claim', r'\b(we are|is) the first\b|first (paper|study) to'),
]


def colon_kind(sent, nxt):
    s = sent.strip()
    if re.match(r'^(摘\s*要|关键词|注|资料来源|假说\s*\w*|H\d+\w?|Panel|表|图|附表)[^：]{0,10}：', s): return 'label'
    after = s.split('：', 1)[1] if '：' in s else ''
    before = s.split('：', 1)[0]
    if re.match(r'\s*(（\d）|\(\d\)|一是|第一|①|1\.)', after) or re.search(r'(如下|以下|[一二三四五六七八九十两\d]+\s*(项|类|个|点|种|条|方面|部分|组)|包括|分别为)', before): return 'list'
    if after.strip() == '': return 'formula'
    if s.endswith('？') or s.endswith('?'): return 'question'
    if re.search(r'(如下|模型|方程|式子)\s*：?\s*$', s) or (after.strip() == '' and nxt is not None and (len(nxt.strip()) < 60 and re.search(r'[=＝β]', nxt))): return 'formula'
    return 'explanatory'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx'); ap.add_argument('--mode', default='ZE', choices=['ZE', 'ZC', 'E'])
    ap.add_argument('--terms'); ap.add_argument('--facts'); ap.add_argument('--out')
    a = ap.parse_args()
    items = read(a.docx)
    body = [it for it in items if it['text'].strip()]
    zh = a.mode in ('ZE', 'ZC')
    R = []
    add = R.append
    add(f'# 检查报告\n\n稿件：`{os.path.basename(a.docx)}`　模式：{a.mode}\n')

    # 参考文献范围
    ref_start = next((k for k, it in enumerate(body) if it['part'] == 'body' and re.fullmatch(r'\s*(参考文献|References)\s*', it['text'])), None)
    main_items = body[:ref_start] if ref_start is not None else body
    refs = [it for it in body[ref_start + 1:] if it['part'] == 'body' and not it['in_table']] if ref_start is not None else []
    prose = [it for it in main_items if not it['in_table']]

    # 1 红线
    add('## 1. 句式红线（language/zh.md §I；language/en.md §5）\n')
    hits = collections.defaultdict(list)
    for it in prose:
        for name, rx in (ZH_RED if zh else EN_RED):
            for m in re.finditer(rx, it['text']):
                if name.startswith('"与') and re.search(r'与(式|表|第)', it['text'][max(0, m.start() - 2):m.end()]): continue
                hits[name].append((loc(it), it['text'][max(0, m.start() - 25):m.end() + 25]))
    if not hits: add('无命中。\n')
    for name, lst in hits.items():
        add(f'- **{name}**：{len(lst)} 处')
        for l, s in lst[:8]: add(f'  - {l}：…{s}…')
    add('')

    # 2 冒号
    if zh:
        add('## 2. 冒号分类（language/zh.md §I 冒号保留口径；ai-tone Z2）\n')
        kinds = collections.Counter(); expl = []
        for k, it in enumerate(prose):
            ss = sents_zh(it['text'])
            if HEAD.match(it['text']) and len(it['text']) < 50: continue
            for j, s in enumerate(ss):
                if '：' not in s: continue
                nxt = ss[j + 1] if j + 1 < len(ss) else (prose[k + 1]['text'] if k + 1 < len(prose) else None)
                kd = colon_kind(s, nxt); kinds[kd] += 1
                if kd == 'explanatory': expl.append((loc(it), s.strip()))
        add(f'- 合计：{dict(kinds)}（列举、公式、问句、标签保留；解释性冒号为 A 级，改句号或逗号加关联词）')
        add('  （以下为整句，供逐条拟改与设问；按 protocol D10 处理，不得只报数量）')
        for l, s in expl[:40]: add(f'  - {l}：{s}')
        add('')

    # 3 节首节末与交叉引用写法
    add('## 3. 节首、节末与交叉引用写法（structure.md §5）\n')
    heads = [(k, it) for k, it in enumerate(prose) if it['part'] == 'body' and HEAD.match(it['text']) and len(it['text']) < 50]
    head_idx = {k for k, _ in heads}
    subj, prev = [], []
    for k, it in enumerate(prose):
        t = it['text']
        if re.search(r'安排如下|organized as follows|rest of (the|this) paper', t): continue
        for s in (sents_zh(t) if zh else sents_en(t)):
            st = s.strip()
            if len(re.findall(r'第\s*\d+(?:\.\d+)*\s*(?:至\s*\d+(?:\.\d+)*\s*)?节', st)) >= 2 and '；' in st: continue  # 章首小节导引（类 ⑥）
            if (zh and re.match(r'^第\s*\d+(\.\d+)*\s*(节|部分)(的|表明|显示|给出|发现|分析|检验)', st)) or (not zh and re.match(r'^Sections? \d+(\.\d+)* (shows?|predicts?|suggests?|finds?|documents?)', st)):
                subj.append((loc(it), st))
        if k + 1 in head_idx or k + 1 == len(prose):
            last = (sents_zh(t) if zh else sents_en(t))[-1:] or ['']
            if re.search(r'下一节|下文将|下一部分|接下来|第\s*\d+\s*节在此基础上|in the next section|next section', last[0], re.I):
                prev.append((loc(it), last[0].strip()[:80]))
    add(f'- 以节号作主语开头：{len(subj)} 处'); [add(f'  - {l}：{s}') for l, s in subj[:20]]
    add(f'- 节末预告下一节：{len(prev)} 处'); [add(f'  - {l}：{s}') for l, s in prev[:20]]
    add('')

    # 4 长句
    add('## 4. 长句（language/zh.md §E；language/en.md §2）\n')
    longs = []
    for it in prose:
        for s in (sents_zh(it['text']) if zh else sents_en(it['text'])):
            n = len(CJK.findall(s)) if zh else len(s.split())
            if n > (100 if zh else 45): longs.append((n, loc(it), s.strip()[:70]))
    longs.sort(reverse=True)
    add(f'- 超过 {"100 字" if zh else "45 词"}：{len(longs)} 句')
    for n, l, s in longs[:15]: add(f'  - {l}（{n}）：{s}…')
    add('')

    # 5 人称与路标
    if zh:
        add('## 5. 人称与路标（language/zh.md §B §C）\n')
        txt = '\n'.join(it['text'] for it in prose)
        we = len(re.findall(r'我们', txt)); bw = len(re.findall(r'本文(发现|认为|研究发现|的结果)', txt))
        add(f'- "我们" {we} 次；"本文发现/本文认为"类结果句 {bw} 次。' + ('ZE 模式结果句应以"我们"领起。' if a.mode == 'ZE' else 'ZC 模式结果句应以"本文"领起。'))
        add(f'- "进一步" {txt.count("进一步")} 次（参考值约 10）；"具体而言" {txt.count("具体而言")} 次（每节至多 1）；"综上" {txt.count("综上")} 次。\n')

    # 6 术语
    if a.terms and os.path.exists(a.terms):
        add('## 6. 一物一名（language/zh.md §F）\n')
        txt = '\n'.join(it['text'] for it in body)
        for line in open(a.terms, encoding='utf8'):
            if '|' not in line or line.startswith('#'): continue
            std, al = [x.strip() for x in line.split("|")[:2]]
            als = [x.strip() for x in re.split(r'[,，、]', al) if x.strip()]
            cnt = {x: txt.count(x) for x in als if txt.count(x)}
            add(f'- {std}：标准名 {txt.count(std)} 次' + (f'；需统一的别名 {cnt}' if cnt else '；无别名'))
        add('')

    # 7 交叉引用存在性
    add('## 7. 交叉引用是否存在（structure.md §5.4）\n')
    sec_nums = {HEAD.match(it['text']).group(1) for _, it in heads}
    alltxt = '\n'.join(it['text'] for it in body)
    tables = set(re.findall(r'(?:^|\n)\s*(?:\[此处插入)?表\s*(\d+)', alltxt)) | set(re.findall(r'(?:^|\n)\s*Table\s+(\d+)', alltxt))
    atables = set(re.findall(r'(?:附表|表|Table)\s*(A\d+)', '\n'.join(it['text'] for it in body if re.match(r'\s*(?:\[此处插入)?(?:附表|表|Table)\s*A\d+', it['text']))))
    cap_style = collections.Counter(re.match(r'\s*(?:\[此处插入)?(附表|表|Table)\s*A\d+', it['text']).group(1) for it in body if re.match(r'\s*(?:\[此处插入)?(?:附表|表|Table)\s*A\d+', it['text']))
    figs = set(re.findall(r'(?:^|\n)\s*(?:\[此处插入)?图\s*(\d+)', alltxt)) | set(re.findall(r'(?:^|\n)\s*Figure\s+(\d+)', alltxt))
    bad = collections.defaultdict(set)
    maintxt = '\n'.join(it['text'] for it in prose)
    for m in re.finditer(r'第\s*(\d+(?:\.\d+)*)\s*(?:至\s*(\d+(?:\.\d+)*)\s*)?节|Sections?\s+(\d+(?:\.\d+)*)', maintxt):
        for g in (m.group(1), m.group(2), m.group(3)):
            if g and g not in sec_nums: bad['节'].add(g)
    for m in re.finditer(r'(?<!附)表\s*(\d+)|Table\s+(\d+)', maintxt):
        g = m.group(1) or m.group(2)
        if g not in tables: bad['表'].add(g)
    for m in re.finditer(r'附表\s*(A\d+)', maintxt):
        if atables and m.group(1) not in atables: bad['附表'].add(m.group(1))
    for m in re.finditer(r'图\s*(\d+)|Figure\s+(\d+)', maintxt):
        g = m.group(1) or m.group(2)
        if g not in figs: bad['图'].add(g)
    add(f'- 识别到的节号 {len(sec_nums)} 个、表 {len(tables)} 个、附表 {len(atables)} 个、图 {len(figs)} 个。')
    txt_style = collections.Counter(m.group(1) for m in re.finditer(r'(附表|附录表)\s*A\d+', maintxt))
    if cap_style and txt_style and set(cap_style) != set(txt_style): add(f'- **附表命名不一致**：标题写作 {dict(cap_style)}，正文引用写作 {dict(txt_style)}（一物一名）')
    if any(bad.values()):
        for k, v in bad.items(): add(f'- **引用了但未找到的{k}**：{sorted(v, key=lambda x: [int(y) if y.isdigit() else y for y in re.split(r"[.A]", x) if y])}')
    else: add('- 所有引用的节、表、附表、图都存在。')
    add('')

    # 8 数字
    add('## 8. 数字（sections/results.md §4 §6）\n')
    two = []
    for it in prose:
        for m in re.finditer(r'(\d+\.\d{2,})\s*(个百分点|%|家)', it['text']):
            two.append((loc(it), it['text'][max(0, m.start() - 20):m.end() + 5]))
    add(f'- 正文效应值保留两位及以上小数：{len(two)} 处（统一一位；样本均值除外，人工判断）')
    for l, s in two[:15]: add(f'  - {l}：…{s}…')
    pct = [(loc(it), it['text'][max(0, m.start() - 25):m.end()]) for it in prose for m in re.finditer(r'(概率|比例|占比|份额|比率)[^。，；]{0,15}(提高|下降|增加|减少)[^。，；]{0,6}\d+(\.\d+)?\s*%', it['text'])]
    add(f'- 份额之差可能误写为 %：{len(pct)} 处'); [add(f'  - {l}：…{s}') for l, s in pct[:10]]
    if a.facts and os.path.exists(a.facts):
        vals = []
        for r in csv.DictReader(open(a.facts, encoding='utf8')):
            for f in ('coef', 'econ_value'):
                v = (r.get(f) or '').strip()
                if v: vals.append((f, r.get('table'), r.get('column'), v))
        miss = [v for v in vals if v[3].lstrip('-') not in alltxt and v[3].replace('-', '−').lstrip('−') not in alltxt]
        add(f'- facts.csv 中的数值 {len(vals)} 个，正文或表格中未找到 {len(miss)} 个：')
        for f, t, c, v in miss[:20]: add(f'  - 表 {t} 第（{c}）列 {f}={v}')
    add('')

    # 9 参考文献
    add('## 9. 参考文献互查（判例 C-24）\n')
    if refs:
        keys_ref = set()
        for it in refs:
            m = re.match(r"\s*([A-Z][A-Za-z'’\-]+(?: [A-Z][a-z]+)?)[^()]*?\((\d{4})[a-z]?\)", it['text'])
            if m: keys_ref.add((m.group(1).split()[0] if ' ' not in m.group(1) or m.group(1).split()[0] not in ('La', 'De', 'Van', 'Von') else m.group(1), m.group(2)))
        keys_cit = set()
        maintext = '\n'.join(it['text'] for it in body if it not in refs)
        for it in main_items:
            for m in re.finditer(r"([A-Z][A-Za-z'’\-]+)(?:,? (?:[A-Z][A-Za-z'’\-]+,? )*(?:and [A-Z][A-Za-z'’\-]+))?(?: et al\.)?(?:,|，)?\s*[（(]?(\d{4})[a-z]?", it['text']):
                if m.group(1) in ('Table', 'Section', 'Panel', 'Figure', 'Appendix', 'Column', 'The', 'In', 'No', 'P'): continue
                keys_cit.add((m.group(1), m.group(2)))
        reftexts = [it['text'][:120] for it in refs]
        def in_refs(name, yr): return any(name in rt and yr in rt for rt in reftexts)
        cited_missing = sorted(k for k in keys_cit if not in_refs(*k))
        uncited = []
        for it in refs:
            m = re.match(r"\s*([^,(]+?),[^()]*?\((\d{4})[a-z]?\)", it['text'])
            if not m: continue
            name = m.group(1).strip().split()[-1] if not m.group(1).strip().startswith(('La ', 'De ', 'Van ', 'Von ')) else m.group(1).strip()
            yr = m.group(2)
            if not re.search(re.escape(name) + r"[^。；;）)]{0,60}" + yr, maintext): uncited.append((name, yr))
        add(f'- 文末列表 {len(keys_ref)} 条；正文引用（作者, 年份）{len(keys_cit)} 组。')
        add(f'- 正文引用但列表中可能缺失：{cited_missing[:30]}')
        add(f'- 列表中有但正文可能未引用：{uncited[:30]}')
        add('- 以上为自动匹配，复合姓氏、机构作者、图注中的引用需人工复核。')
    else:
        add('- 未找到"参考文献/References"标题，跳过。')
    out = '\n'.join(R) + '\n'
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, 'w', encoding='utf8').write(out); print('写入', a.out)
    else:
        print(out)


if __name__ == '__main__':
    main()
