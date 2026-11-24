import json,re,collections
exec(open('frames.py').read().split("out={}")[0])
for lang in ['en','zh']:
    zh=lang=='zh'; G=[p for p in P if p['lang']==lang and good(p)]
    print('\n####',lang)
    for c in CATS:
        T=[x for p in G for ch in p['chap'] for cc,ps in [(ch['cat'],ch['paras'])]+[(s['cat'],s['paras']) for s in ch['subs']] if cc==c for x in ps if clean(x,zh)]
        if not T: continue
        S=[s for x in T for s in sents(x,zh)]; L=[size(s,zh) for s in S]; tot=sum(size(x,zh) for x in T)
        if zh:
            r=lambda rx: round(1000*sum(len(re.findall(rx,x)) for x in T)/tot,2)
            print(f' {c:12s} sents={len(S)} >100字 {100*sum(l>100 for l in L)/len(L):.1f}% >80字 {100*sum(l>80 for l in L)/len(L):.1f}% ≤40字 {100*sum(l<=40 for l in L)/len(L):.0f}% | 我们/千字 {r("我们")} 本文/千字 {r("本文")} | 冒号句占比 {100*sum("：" in s for s in S)/len(S):.1f}% | 进一步 {r("进一步")} 具体而言 {r("具体而言")} 表明 {r("表明")}')
        else:
            r=lambda rx: round(1000*sum(len(re.findall(rx,x,re.I)) for x in T)/tot,2)
            WE=r(r"\b(we|our|us)\b"); TP=r(r"this (paper|study|article)"); IS=r(r"in this section"); CW=r(r"consistent with"); SG=r(r"\bsuggests?\b")
            HW=round(1000*sum(s.startswith("However") for s in S)/tot,2); MO=round(1000*sum(bool(re.match(r"(Moreover|Furthermore|Additionally|In addition)",s)) for s in S)/tot,2)
            g40=100*sum(l>40 for l in L)/len(L); s12=100*sum(l<12 for l in L)/len(L)
            print(f" {c:12s} sents={len(S)} >40w {g40:.1f}% <12w {s12:.1f}% | we/our/us {WE} | this paper {TP} | in this section {IS} | consistent with {CW} | suggest {SG} | However {HW} | Moreover etc {MO}")
