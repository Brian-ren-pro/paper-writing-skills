import json,re,statistics,collections,os
K=json.load(open('kept.json'))
exec(open('segment.py').read().split('def cat')[0].split("K=json.load")[1].split('\n',1)[1])  # loads CAT_EN, CAT_ZH
def cat(h,zh):
    h2=h.lower()
    for c,p in (CAT_ZH if zh else CAT_EN):
        if re.search(p,h2): return c
    return 'other'
ROMAN='IVX'
def head_en(s):
    s=s.strip()
    if len(s)>90 or s.endswith(('.',',',';')) and not re.match(r'^[IVX]+\.\s',s): 
        if not re.match(r'^(\d{1,2}|[IVX]{1,5})\.\s+[A-Z][A-Za-z ,:\-–’\']{2,80}$',s): return None
    m=re.match(r'^(?:(\d{1,2})(\.\d{1,2})?\.?|([IVX]{1,5})\.|([A-H])\.)\s*\|?\s+([A-Z][A-Za-z0-9 ,:;\-–—’\'&/()]{2,85})$',s)
    if m:
        lvl=2 if (m.group(2) or m.group(4)) else 1
        h=m.group(5)
        if len(h.split())>12 or re.search(r'\b(Table|Figure|Panel)\b',h): return None
        if lvl==1 and m.group(1) and int(m.group(1))>12: return None
        return lvl,h
    if re.fullmatch(r'(Introduction|INTRODUCTION|Conclusions?|CONCLUSIONS?|Concluding Remarks)',s): return 1,s
    return None
def head_zh(s):
    s=re.sub(r'\s+','',s)
    m=re.fullmatch(r'([一二三四五六七八九十]{1,2})[、.．](\S{2,28})',s)
    if m and not re.search(r'[，。；]',m.group(2)): return 1,m.group(2)
    m=re.fullmatch(r'[（(]([一二三四五六七八九十]{1,2})[）)](\S{2,28})',s)
    if m and not re.search(r'[，。；]',m.group(2)): return 2,m.group(2)
    return None
END=re.compile(r'[.?!:。？！：”"）)]\s*$')
res=[]
for o in K:
    zh=o['lang']=='zh'
    raw=open('raw/'+os.path.basename(o['fn'])).read().replace('\f','\n')
    lines=raw.split('\n')
    merged=[]; i=0
    while i<len(lines):
        l=lines[i]
        if re.fullmatch(r'\s*([IVX]{1,4}|[A-H])\.\s*',l):
            j=i+1
            while j<len(lines) and j<i+4 and not lines[j].strip(): j+=1
            if j<len(lines) and 2<len(lines[j].strip())<85 and re.match(r'[A-Z]',lines[j].strip()) and not lines[j].strip().endswith('.'):
                merged.append(l.strip()+' '+lines[j].strip()); i=j+1; continue
        merged.append(l); i+=1
    lines=merged
    # cut references
    for i in range(len(lines)-1,len(lines)//3,-1):
        if re.fullmatch(r'\s*(References|REFERENCES|参考文献|Bibliography)\s*',lines[i]): lines=lines[:i]; break
    secs=[]; cur=dict(level=1,head='__pre__',cat='pre',lines=[]); secs.append(cur)
    for l in lines:
        h=(head_zh if zh else head_en)(l) if l.strip() else None
        if h:
            lvl,hd=h
            cur=dict(level=lvl,head=hd,cat=cat(hd,zh),lines=[]); 
            if lvl==2: cur['parent']=next((x['cat'] for x in reversed(secs) if x['level']==1),None)
            secs.append(cur); continue
        cur['lines'].append(l)
    for s in secs:
        L=s['lines']; nonb=[len(x.strip()) for x in L if len(x.strip())>(8 if zh else 20)]
        med=statistics.median(nonb) if nonb else 60
        paras=[]; buf=[]
        for x in L:
            t=x.strip()
            if not t:
                if buf and END.search(buf[-1]): paras.append(buf); buf=[]
                continue
            buf.append(t)
            if len(t)<0.7*med and END.search(t): paras.append(buf); buf=[]
        if buf: paras.append(buf)
        out=[]
        for p in paras:
            txt=(''.join(p) if zh else ' '.join(p))
            txt=re.sub(r'-\s+(?=[a-z])','',txt) if not zh else txt
            txt=re.sub(r'\s+',' ',txt).strip()
            if len(txt)>(60 if zh else 200) and not re.match(r'^(Table|Figure|表|图)\s?\d',txt): out.append(txt)
        s['paras']=out; del s['lines']
    full=raw[:40000]
    if zh: m=re.search(r'摘\s*要[:：]?(.{50,900}?)(关\s*键\s*词|Key\s*words)',re.sub(r'\s+','',full))
    else: m=re.search(r'(?:ABSTRACT|Abstract)[\s:.\-—]*(.{300,2500}?)(?:\n\s*\n|JEL|Keywords|Key words|KEYWORDS)',full,re.S)
    abstract=re.sub(r'\s+','' if zh else ' ',m.group(1)).strip() if m else ''
    # intro fallback: if no introduction heading, take 'pre' paragraphs after abstract
    if not any(s['cat']=='introduction' for s in secs) and secs[0]['paras']:
        pre=secs[0]['paras']; 
        if abstract:
            k=next((i for i,p in enumerate(pre) if abstract[:40] in p),-1); pre=pre[k+1:]
        secs[0]['cat']='introduction_guess'; secs[0]['paras']=pre
    res.append(dict(j=o['j'],tier=o['tier'],t=o['t'],d=o['d'],lang=o['lang'],abstract=abstract,secs=secs))
json.dump(res,open('seg.json','w'),ensure_ascii=False)
c=collections.Counter()
for r in res:
    cats=[s['cat'] for s in r['secs'] if s['level']==1]
    c[(r['lang'],'intro' if 'introduction' in cats else 'guess' if 'introduction_guess' in cats else 'none', 'concl' if 'conclusion' in cats else 'noconcl')]+=1
print(c)
