import json,re,statistics,collections
K=json.load(open('kept.json'))
CAT_EN=[('conclusion',r'conclu|concluding|summary and'),('introduction',r'^introduction'),('robustness',r'robust|sensitivity|alternative (explanation|specification|measure)|placebo|additional test'),
('mechanism',r'mechanism|channel|heterogene|cross-section|why|economic sources|further (analys|evidence|test)|additional (analys|result|evidence)|extension'),
('theory',r'hypothes|theor|model|conceptual|framework|prediction|motivation'),('background',r'institutional|background|setting|regulat|policy|law|reform'),
('literature',r'literature|related (work|research|studies)|prior research'),('data',r'^data|data and|sample|variable|measure|descriptive|summary stat'),
('design',r'empirical (strategy|design|method|model|specification|framework|approach)|identification|research design|methodolog|estimation|econometric'),
('results',r'result|finding|evidence|baseline|main|analysis|effect|impact')]
CAT_ZH=[('conclusion',r'结论|结语|研究结论|政策建议'),('introduction',r'引言|问题的提出|引论'),('robustness',r'稳健'),('mechanism',r'机制|渠道|异质|进一步|拓展|扩展'),
('theory',r'理论|假说|假设'),('background',r'制度背景|政策背景|背景'),('literature',r'文献'),('data',r'数据|样本|变量'),('design',r'研究设计|模型|实证策略|识别|方法'),('results',r'结果|实证分析|基准|检验|回归')]
def cat(h,zh):
    h2=h.lower()
    for c,p in (CAT_ZH if zh else CAT_EN):
        if re.search(p,h2): return c
    return 'other'
H1_EN=re.compile(r'^\s{0,20}(?:(\d{1,2})\.?|([IVX]{1,5})\.)\s+([A-Z][A-Za-z0-9 ,:;\-–—’\'&/()]{2,90}?)\s*$')
H2_EN=re.compile(r'^\s{0,20}(?:(\d{1,2})\.(\d{1,2})\.?|([A-H])\.)\s+([A-Z][A-Za-z0-9 ,:;\-–—’\'&/()]{2,90}?)\s*$')
H1_ZH=re.compile(r'^\s{0,20}([一二三四五六七八九十]{1,2})\s*[、.．]\s*(\S.{1,28}?)\s*$')
H2_ZH=re.compile(r'^\s{0,20}[（(]([一二三四五六七八九十]{1,2})[）)]\s*(\S.{1,28}?)\s*$')
res=[]
for o in K:
    zh=o['lang']=='zh'
    lines=open(o['fn']).read().replace('\f','\n').split('\n')
    # abstract
    full='\n'.join(lines)
    secs=[]; cur=None
    for i,l in enumerate(lines):
        s=l.strip()
        if not s: 
            if cur: cur['lines'].append('')
            continue
        m1=(H1_ZH if zh else H1_EN).match(l); m2=(H2_ZH if zh else H2_EN).match(l)
        if m1 and len(s)<(40 if zh else 95) and not s.endswith(('.',',')) :
            head=m1.group(2) if zh else m1.group(3)
            if not zh and (len(head.split())>12 or head.isupper() and len(head)<4): pass
            else:
                cur=dict(level=1,head=head,cat=cat(head,zh),lines=[]); secs.append(cur); continue
        if m2 and cur and len(s)<(40 if zh else 95) and not s.endswith(('.',',')):
            head=m2.group(2) if zh else m2.group(4)
            if zh or len(head.split())<=12:
                cur=dict(level=2,head=head,cat=cat(head,zh),parent=next((x['cat'] for x in reversed(secs) if x['level']==1),None),lines=[]); secs.append(cur); continue
        if cur: cur['lines'].append(l)
    # abstract
    if zh: m=re.search(r'摘\s*要[:：]?(.{50,800}?)(关键词|关 键 词|Key\s*words)',re.sub(r'\s+','',full[:20000]))
    else: m=re.search(r'(?:ABSTRACT|Abstract)[\s:.\-—]*(.{300,2500}?)(?:\n\s*\n|JEL|Keywords|Key words|\*)',full[:30000],re.S)
    abstract=re.sub(r'\s+',' ',m.group(1)).strip() if m else ''
    # first-level sanity: keep paper only if has intro and >=3 level1
    l1=[s for s in secs if s['level']==1]
    # paragraphs
    for s in secs:
        L=s['lines']; body=[x for x in L if x.strip()]
        if not body: s['paras']=[]; del s['lines']; continue
        ind=[len(x)-len(x.lstrip()) for x in body]; base=statistics.mode(ind)
        paras=[]; buf=[]; prev=''
        for x in L:
            if not x.strip():
                if buf and re.search(r'[.?!。？！”"）)]\s*$',buf[-1]): paras.append(' '.join(buf)); buf=[]
                continue
            n=len(x)-len(x.lstrip())
            if buf and n>=base+2 and n<=base+10 and re.search(r'[.?!。？！”"）)]\s*$',prev):
                paras.append(' '.join(buf)); buf=[]
            buf.append(x.strip()); prev=x
        if buf: paras.append(' '.join(buf))
        sep='' if zh else ' '
        s['paras']=[re.sub(r'\s+',' ' if not zh else '',p).strip() for p in paras if len(p)>(60 if zh else 150)]
        del s['lines']
    res.append(dict(j=o['j'],tier=o['tier'],t=o['t'],d=o['d'],lang=o['lang'],abstract=abstract,n_l1=len(l1),secs=secs))
json.dump(res,open('seg.json','w'),ensure_ascii=False)
c=collections.Counter(); 
for r in res:
    cats={s['cat'] for s in r['secs'] if s['level']==1}
    c[(r['lang'],'has_intro' if 'introduction' in cats else 'no_intro')]+=1
print(len(res),c)
