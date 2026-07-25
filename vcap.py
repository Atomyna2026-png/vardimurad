import re, sys, shutil
F="index.html"
s=open(F,encoding="utf-8").read(); orig=s
prob=[]

s2=re.sub(r'\.vtile\{[^}]*\}',
""".vcard{display:flex;flex-direction:column;gap:10px;cursor:pointer}
.vtile{position:relative;overflow:hidden;background:#15151a;aspect-ratio:16/9;border:1px solid rgba(255,255,255,.10);transition:border-color .3s ease,transform .3s ease}
.vcard:hover .vtile{border-color:rgba(255,255,255,.30);transform:translateY(-4px)}""",
s,count=1)
if s2==s: prob.append(".vtile rule")
s=s2
s=re.sub(r'\.vtile \.vov\{[^}]*\}\n?','',s)
s=re.sub(r'\.vtile span\{[^}]*\}',
         ".vcap{font-family:var(--fb);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);transition:color .25s ease}\n.vcard:hover .vcap{color:var(--cream)}",
         s,count=1)

pairs=[
("var t=document.createElement('div');t.className='tile vtile';",
 "var c=document.createElement('div');c.className='vcard';\n    var t=document.createElement('div');t.className='vtile';c.appendChild(t);"),
("var lb=document.createElement('span');lb.textContent='Video '+s;t.appendChild(lb);",
 "var lb=document.createElement('div');lb.className='vcap';lb.textContent='Video '+s;c.appendChild(lb);"),
("g.appendChild(t);","g.appendChild(c);"),
]
for old,new in pairs:
    if s.count(old)!=1: prob.append(old[:40])
    else: s=s.replace(old,new,1)
s=re.sub(r"\s*var o=document\.createElement\('div'\);o\.className='vov';t\.appendChild\(o\);",'',s)

if prob: sys.exit("NOTHING CHANGED. Missing: "+", ".join(prob))
shutil.copy(F,F+".bakcap")
open(F,"w",encoding="utf-8").write(s)
print("Gold frames removed; titles now sit under each video. %d -> %d bytes"%(len(orig),len(s)))
