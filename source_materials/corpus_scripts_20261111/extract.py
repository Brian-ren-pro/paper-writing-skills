import json,subprocess,re,os,sys,time
L=json.load(open('list.json')); H=os.environ['HOME']+'/mnt/Zotero/storage/'
os.makedirs('txt',exist_ok=True)
keep=json.load(open('kept.json')) if os.path.exists('kept.json') else []
done=json.load(open('done.json')) if os.path.exists('done.json') else []
seen={(re.sub(r'\W+','',o['t'].lower())[:60],o['lang']) for o in keep}
t0=time.time()
for i,o in enumerate(L):
    if i in done: continue
    if time.time()-t0>150: break
    done.append(i)
    key=re.sub(r'\W+','',o['t'].lower())[:60]
    try: txt=subprocess.run(['pdftotext','-layout',H+o['f'],'-'],capture_output=True,text=True,timeout=40).stdout
    except Exception: continue
    cjk=len(re.findall(r'[一-鿿]',txt[:30000])); lang='zh' if cjk>3000 else 'en'
    if (o['tier']=='zh')!=(lang=='zh') or (key,lang) in seen or len(txt)<15000: continue
    seen.add((key,lang)); fn=f'txt/{i:04d}.txt'; open(fn,'w').write(txt); o.update(lang=lang,fn=fn); keep.append(o)
json.dump(keep,open('kept.json','w'),ensure_ascii=False); json.dump(done,open('done.json','w'))
print('done',len(done),'/',len(L),'kept',len(keep))
