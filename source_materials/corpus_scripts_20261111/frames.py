import json,re,collections
exec(open('check.py').read().split("R={}")[0])
def clean(x,zh):
    if re.search(r'Downloaded|https?:|Electronic copy|doi\.org|Yes\s+Yes|YES|〔\d|Electronic|ＹＥＳ|Ｙｅｓ|是是是',x): return False
    if zh: return len(re.findall(r'[一-鿿]',x))/max(len(x),1)>0.6 and len(x)>80
    return len(re.findall(r'[A-Za-z ]',x))/max(len(x),1)>0.85 and len(x.split())>40
out={}
for lang in ['en','zh']:
    zh=lang=='zh'; G=[p for p in P if p['lang']==lang and good(p)]
    print(f'\n######## {lang.upper()}')
    for c in CATS:
        op=collections.Counter(); fr=collections.Counter(); tot=0; ns=0
        for p in G:
            for ch in p['chap']:
                for cc,ps in [(ch['cat'],ch['paras'])]+[(s['cat'],s['paras']) for s in ch['subs']]:
                    if cc!=c: continue
                    for x in ps:
                        if not clean(x,zh): continue
                        tot+=1
                        if zh:
                            op[x[:4]]+=1
                            for s in sents(x,zh):
                                ns+=1; fr[re.sub(r'[\d０-９]','N',s.strip()[:5])]+=1
                        else:
                            op[' '.join(x.split()[:3])]+=1
                            for s in sents(x,zh):
                                ns+=1; fr[re.sub(r'\b\d+\b','N',' '.join(s.split()[:3]))]+=1
        print(f'== {c}: paras={tot}, sents={ns}')
        print('   para openers:',' | '.join(f'{k}({v})' for k,v in op.most_common(18)))
        print('   sentence openers:',' | '.join(f'{k}({v})' for k,v in fr.most_common(22)))
