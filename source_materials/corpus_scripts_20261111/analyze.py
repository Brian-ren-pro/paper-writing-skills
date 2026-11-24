import json,re,statistics as st,collections,sys
P=json.load(open('papers.json'))
exec(open('stats.py').read().split('def sents')[1].split('papers=[]')[0].join(['def sents','']) if False else '')
def sents(t,zh):
    if zh: return [s for s in re.split(r'(?<=[。！？])',t) if len(s)>4]
    t=re.sub(r'\b(et al|e\.g|i\.e|cf|vs|Fig|No|Eq|Inc|U\.S|Jr)\.',lambda m:m.group(0).replace('.','§'),t)
    return [s.replace('§','.') for s in re.split(r'(?<=[.?!])\s+(?=[A-Z(“"])',t) if len(s)>15]
def size(t,zh): return len(re.findall(r'[一-鿿]',t)) if zh else len(re.findall(r"[A-Za-z][A-Za-z'\-]*",t))
def q(v):
    v=[x for x in v if x is not None]
    if not v: return 'n=0'
    if len(v)<4: return f'n={len(v)} med={st.median(v):.0f}'
    a=st.quantiles(v,n=4); return f'n={len(v)} med={st.median(v):.0f} IQR=[{a[0]:.0f},{a[2]:.0f}]'
CATS=['introduction','background','literature','theory','data','design','results','robustness','mechanism','conclusion']
def chapter_paras(p,c):  # level-1 chapter incl its subs
    out=[]
    for ch in p['chap']:
        if ch['cat']==c: out+= ch['paras']+[x for s in ch['subs'] for x in s['paras']]
    return out
def content_paras(p,c):
    out=[]
    for ch in p['chap']:
        if ch['cat']==c: out+=ch['paras']+[x for s in ch['subs'] if s['cat'] in (c,'other') for x in s['paras']]
        else: out+=[x for s in ch['subs'] if s['cat']==c for x in s['paras']]
    return out
for lang in ['en','zh']:
    G=[p for p in P if p['lang']==lang]; zh=lang=='zh'
    print(f'\n######## {lang.upper()}  papers={len(G)}  ({collections.Counter(p["tier"] for p in G)})')
    # structure
    seqs=collections.Counter(); pres=collections.Counter(); nl1=[]
    for p in G:
        cats=[c['cat'] for c in p['chap']]; nl1.append(len(cats))
        for c in set(cats): pres[c]+=1
        subcats={s['cat'] for ch in p['chap'] for s in ch['subs']}
        for c in ['robustness','mechanism','background','literature','theory']:
            if c not in cats and c in subcats: pres[c+'(sub only)']+=1
        seq=[]; 
        for c in cats:
            if c in CATS and (not seq or seq[-1]!=c): seq.append(c)
        seqs[' > '.join(seq)]+=1
    print('level-1 sections:',q(nl1))
    print('chapter presence (level-1):',{k:f'{v}/{len(G)}' for k,v in sorted(pres.items(),key=lambda x:-x[1])})
    print('top sequences:'); [print('  ',v,k) for k,v in seqs.most_common(8)]
    # per category
    print('-- per chapter length / paragraphs / para length / sentence length')
    for c in CATS:
        L=[];NP=[];PL=[];SL=[]
        for p in G:
            ps=chapter_paras(p,c) if c not in('robustness','mechanism') else content_paras(p,c)
            if not ps: continue
            t=' '.join(ps); L.append(size(t,zh)); NP.append(len(ps)); PL+= [size(x,zh) for x in ps]
            SL+=[size(s,zh) for s in sents(t,zh)]
        print(f'  {c:12s} len {q(L)} | paras {q(NP)} | para_len {q(PL)} | sent_len {q(SL)}')
    # abstract
    A=[p['abstract'] for p in G if p['abstract']]
    print('-- abstract: len',q([size(a,zh) for a in A]),'| sentences',q([len(sents(a,zh)) for a in A]),
          '| with citation',sum(bool(re.search(r'\(\D*\d{4}\)|（\D*\d{4}）|et al',a)) for a in A),'/',len(A),
          '| with numbers',sum(bool(re.search(r'\d+(\.\d+)?\s?(%|percent|个百分点|basis|bp)',a)) for a in A),'/',len(A))
