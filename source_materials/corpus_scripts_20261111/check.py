import json,re,statistics as st,collections
P=json.load(open('papers.json'))
exec(open('analyze.py').read().split("CATS=")[0].split("exec(")[0]+'\n'+open('analyze.py').read().split("exec(open('stats.py')")[1].split('\n',1)[1].split('CATS=')[0])
CATS=['introduction','background','literature','theory','data','design','results','robustness','mechanism','conclusion']
STOP=re.compile(r'^(Appendix|APPENDIX|Acknowledg|ACKNOWLEDG|Data Availability|DATA AVAILABILITY|Declaration|Funding|Supplementary|附录|致谢|参考文献)')
def clean_concl(ps,zh):
    out=[]
    for x in ps:
        if STOP.match(x): break
        if size(x,zh)>=(40 if zh else 35): out.append(x)
    return out
def good(p):
    cats={c['cat'] for c in p['chap']}
    intro=sum(size(' '.join(c['paras']+[x for s in c['subs'] for x in s['paras']]),p['lang']=='zh') for c in p['chap'] if c['cat']=='introduction')
    lo,hi=(800,5000) if p['lang']=='en' else (1000,6000)
    return lo<=intro<=hi and 'conclusion' in cats and len(cats&set(CATS))>=4
R={}
for lang in ['en','zh']:
    zh=lang=='zh'; G=[p for p in P if p['lang']==lang and good(p)]
    print(f'\n######## {lang.upper()} well-segmented papers: {len(G)}')
    def chap(p,c): 
        return [x for ch in p['chap'] if ch['cat']==c for x in ch['paras']+[y for s in ch['subs'] for y in s['paras']]]
    # INTRO
    I=[chap(p,'introduction') for p in G]
    print('INTRO words',q([size(' '.join(x),zh) for x in I]),'paras',q([len(x) for x in I]))
    fp=re.compile(r'我们发现|本文发现|研究发现|结果(显示|表明)|we find|our results (show|indicate|suggest)|we show|we document',re.I)
    cp=re.compile(r'贡献|contribut',re.I); rm=re.compile(r'(其余|余下|后续)部分|安排如下|结构安排|remainder of (this|the) paper|rest of (this|the) paper|(paper|article) (is|proceeds|proceed) (organized|structured|as follows)|organized as follows',re.I)
    pos_f=[];pos_c=[];has_rm=0;thispaper=[]
    for ps in I:
        n=len(ps)
        if n<4: continue
        k=next((i for i,x in enumerate(ps) if fp.search(x)),None); pos_f.append(None if k is None else 100*k/n)
        k=next((i for i,x in enumerate(ps) if cp.search(x)),None); pos_c.append(None if k is None else 100*k/n)
        has_rm+=any(rm.search(x) for x in ps[-3:])
        k=next((i+1 for i,x in enumerate(ps) if re.search(r'本文|this paper|this study|in this paper|we (study|examine|investigate|exploit|use)',x,re.I)),None); thispaper.append(k)
    print('  first result para at %',q(pos_f),'| contribution first at %',q(pos_c),'| roadmap in last 3 paras',has_rm,'/',len(I),'| "this paper/we study" first para#',q(thispaper))
    # identification difficulty -> next sentence
    # THEORY: hypotheses count
    H=[]
    for p in G:
        t=' '.join(chap(p,'theory')+chap(p,'introduction'))
        hs=set(re.findall(r'\b(H\d[a-c]?)\b|Hypothesis\s+(\d[a-c]?)|假说\s?(\d[a-c]?)|假设\s?(\d[a-c]?)|H(\d[a-c]?)[：:]',t))
        ids={next(g for g in h if g) for h in hs}
        if chap(p,'theory'): H.append(len(ids))
    print('THEORY hypotheses per paper (with theory chapter):',q(H),collections.Counter(H).most_common(6))
    # CONCLUSION
    C=[clean_concl(chap(p,'conclusion'),zh) for p in G]
    C=[c for c in C if c]
    print('CONCL words',q([size(' '.join(c),zh) for c in C]),'paras',q([len(c) for c in C]), collections.Counter(min(len(c),6) for c in C).most_common())
    fut=re.compile(r'future research|future work|further research|留待|未来研究|今后研究|进一步研究|有待'); lim=re.compile(r'limitation|caveat|局限|不足'); pol=re.compile(r'polic|regulat|政策|监管|建议|启示'); num=re.compile(r'\d+(\.\d+)?\s?(%|percent|个百分点|basis point)')
    for nm,rx in [('future research',fut),('limitation',lim),('policy',pol),('effect numbers',num)]:
        print(f'  concl has {nm}:',sum(bool(rx.search(' '.join(c),) if nm!='future research' else rx.search(' '.join(c).lower())) for c in C),'/',len(C))
    # ABSTRACT
    A=[p['abstract'] for p in G if p['abstract']]
    print('ABSTRACT n',len(A),'len',q([size(a,zh) for a in A]),'sent',q([len(sents(a,zh)) for a in A]),
      '| any digit',sum(bool(re.search(r'\d',a)) for a in A),'| effect number',sum(bool(num.search(a)) for a in A),'| sample/period number',sum(bool(re.search(r'\b(19|20)\d{2}\b|\d{1,3}(,\d{3})+|\d+\s?(firms|banks|loans|countries|家|个|项|年)',a)) for a in A))
    # SECTION OPENERS (first sentence of level1 chapters except intro, and of subsections)
    op=collections.Counter(); ex=collections.defaultdict(list); ends=collections.Counter(); n=0
    pats_en=[('section-number subject',r'^(Section|Sections)\s+\d'),('this section',r'^(In )?this section|^This (section|part)'),('we/our',r'^(We|Our)\b'),('to-purpose',r'^To\s+\w+'),('table/figure',r'^(Table|Figure|Panel|Column)s?\b'),('as discussed in section',r'(As|as) (discussed|shown|described|noted|outlined|argued|explained) in Section'),('in section N, we',r'^In Section \d')]
    pats_zh=[('第X节/上文 作主语',r'^(第[一二三四五六七八九十\d]+(节|部分)|上文|前文|上一节)'),('本节/本部分',r'^本(节|部分)'),('我们/本文',r'^(我们|本文)'),('为了',r'^为(了)?'),('表/图',r'^(表|图)\s?\d'),('根据/基于前文',r'^(根据|基于|结合)(前文|上文|理论|假说)')]
    for p in G:
        for ch in p['chap']:
            if ch['cat'] in ('introduction','other','pre'): continue
            units=[ch['paras']]+[s['paras'] for s in ch['subs']]
            for ps in units:
                if not ps: continue
                n+=1; f=sents(ps[0],zh)[:1]; f=f[0] if f else ps[0][:80]
                for nm,rx in (pats_zh if zh else pats_en):
                    if re.search(rx,f): op[nm]+=1; 
                l=sents(ps[-1],zh)[-1:] ; l=l[0] if l else ''
                if re.search(r'next section|following section|Section \d (examines|presents|discusses|tests|studies|reports)|下一节|下一部分|下文将|接下来',l,re.I): ends['preview next']+=1
    print('SECTION/SUBSECTION openers (n=%d units):'%n,dict(op.most_common()),'| ends with next-section preview:',ends['preview next'])
    # RESULTS: magnitude style
    rs=[' '.join(chap(p,'results')) for p in G if chap(p,'results')]
    def per(rx,texts,unit=1000): 
        tot=sum(size(t,zh) for t in texts); return round(unit*sum(len(re.findall(rx,t,re.I)) for t in texts)/max(tot,1),2)
    if not zh:
        print('RESULTS per 1k words: "standard deviation"',per(r'standard deviation',rs),'| "percentage point"',per(r'percentage point',rs),'| "% of the (sample )?mean|relative to the mean"',per(r'of the (sample |unconditional )?mean|relative to the (sample )?mean',rs),'| "economically significant"',per(r'economically (significant|meaningful|large)',rs),'| "consistent with"',per(r'consistent with',rs))
    else:
        print('RESULTS per 1k chars: 标准差',per(r'标准差',rs),'| 个百分点',per(r'个百分点',rs),'| 均值',per(r'均值',rs),'| 经济(意义|显著)',per(r'经济(意义|显著)',rs),'| 与…一致',per(r'与[^。，]{0,20}一致',rs),'| 表明',per(r'表明',rs),'| 说明',per(r'说明',rs),'| 指向',per(r'指向',rs))
    R[lang]=G
