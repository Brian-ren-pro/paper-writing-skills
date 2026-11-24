import json,re,statistics as st,collections
S=json.load(open('seg.json'))
def norm(h):
    if re.fullmatch(r'[A-Z ]+',h) and h.count(' ')>len(h)/4: h=h.replace(' ','')
    return h
exec(open('segment2.py').read().split('ROMAN=')[0].split('exec(')[0])  # imports
exec(open('segment.py').read().split('def cat')[0].split("K=json.load")[1].split('\n',1)[1])
CAT_EN.insert(2,('robustness',r'endogen|alternative explanation|parallel trend|pre-trend|validity'))
CAT_ZH.insert(2,('robustness',r'内生|替代性解释|安慰剂|平行趋势'))
def cat(h,zh):
    h2=norm(h).lower()
    for c,p in (CAT_ZH if zh else CAT_EN):
        if re.search(p,h2): return c
    return 'other'
def sents(t,zh):
    if zh: return [s for s in re.split(r'(?<=[。！？])',t) if len(s)>4]
    t=re.sub(r'\b(et al|e\.g|i\.e|cf|vs|Fig|No|Eq|Inc|U\.S|Jr)\.',lambda m:m.group(0).replace('.','§'),t)
    return [s.replace('§','.') for s in re.split(r'(?<=[.?!])\s+(?=[A-Z(“"])',t) if len(s)>15]
def size(t,zh): return len(re.findall(r'[一-鿿]',t)) if zh else len(re.findall(r"[A-Za-z][A-Za-z'\-]*",t))
papers=[]
for r in S:
    zh=r['lang']=='zh'; secs=r['secs']; chap=[]  # list of [cat, head, paras, first_sentence_of_section, subsections]
    for s in secs:
        c=s['cat'] if s['cat'] in('pre','introduction_guess') else cat(s['head'],zh)
        if s['level']==1:
            chap.append(dict(cat=c,head=s['head'],paras=list(s['paras']),subs=[]))
        else:
            if not chap: continue
            sc=c if c!='other' else chap[-1]['cat']
            chap[-1]['subs'].append(dict(cat=sc,head=s['head'],paras=s['paras']))
    if chap and chap[0]['cat']=='pre': chap=chap[1:]
    if chap and chap[0]['cat']=='introduction_guess': chap[0]['cat']='introduction'
    papers.append(dict(j=r['j'],tier=r['tier'],lang=r['lang'],t=r['t'],d=r['d'],abstract=r['abstract'],chap=chap))
json.dump(papers,open('papers.json','w'),ensure_ascii=False)
print(len(papers))
