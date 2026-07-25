import sys, shutil
F="index.html"
s=open(F,encoding="utf-8").read(); orig=s
prob=[]

pairs=[
("var VCOUNT=12;",
 "var VCOUNT=12;\nvar VTITLES={1:'Alina Pash - Black Hearse',2:'Alina Pash - Black Hearse'};"),
("lb.textContent='Video '+s;",
 "lb.textContent=VTITLES[i]||('Video '+s);"),
]
for old,new in pairs:
    if s.count(old)!=1: prob.append(old[:40])
    else: s=s.replace(old,new,1)

if prob: sys.exit("NOTHING CHANGED. Missing: "+", ".join(prob))
shutil.copy(F,F+".baktitles")
open(F,"w",encoding="utf-8").write(s)
print("Slots 1 and 2 titled. %d -> %d bytes"%(len(orig),len(s)))
