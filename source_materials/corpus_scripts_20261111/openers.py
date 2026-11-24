import json,re,collections
exec(open('check.py').read().split("R={}")[0])
for lang in ['en','zh']:
    zh=lang=='zh'; G=[p for p in P if p['lang']==lang and good(p)]
    print(f'\n######## {lang.upper()} paragraph openers by chapter (top), n papers={len(G)}')
    for c in CATS:
        cnt=collections.Counter(); tot=0
        for p in G:
            for ch in p['chap']:
                parts=[(ch['cat'],ch['paras'])]+[(s['cat'],s['paras']) for s in ch['subs']]
                for cc,ps in parts:
                    if cc!=c: continue
                    for x in ps:
                        tot+=1
                        if zh: k=re.sub(r'[，,].*','',x[:8])[:4]
                        else:
                            w=re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+",x)[:2]; k=' '.join(w)
                            k=re.sub(r'\b\d+\b','N',k)
                        cnt[k]+=1
        if tot: print(f'  {c} (paras={tot}):',', '.join(f'{k}:{v}' for k,v in cnt.most_common(14)))
    if not zh:
        T=' '.join(x for p in G for ch in p['chap'] for x in ch['paras']+[y for s in ch['subs'] for y in s['paras']])
        for nm,rx in [('one-SD increase in X',r'one[- ]standard[- ]deviation (increase|decrease|change|rise)|a (one )?standard deviation (increase|decrease|change)'),('SD of dependent var / % of SD',r'(of|relative to) (the|its|one) (sample )?standard deviation|standard deviation of (the )?(dependent|outcome)|of a standard deviation'),('% of mean',r'(of|relative to) the (sample |unconditional )?mean'),('percentage points',r'percentage points?'),('basis points',r'basis points?')]:
            print('  magnitude style',nm,len(re.findall(rx,T,re.I)))
