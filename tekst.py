import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import pandas as pd
import re
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
def csvr(f):
    reader=csv.DictReader(f,delimiter=',')
    for line in reader:
        s=line["tt"]+line["type"]+' '+line["ru"]
        s=s.split(' ')
        s=' '.join(s)
        print(s)
        input()
with open('res_ttru.txt') as ttrufile:#[|tt|type|ru|],'r', encoding="utf8"
    reader=csv.reader(ttrufile,delimiter=',')
    ttru=list(map(tuple,reader))
with open('res_rucv.txt') as rucvfile:#[|cv|type|ru|],'r', encoding="utf8"
    reader=csv.reader(rucvfile,delimiter=',')
    rucv=list(map(tuple,reader))
with open('res_rutt.txt') as ruttfile:#[|tt|type|ru|]
    reader=csv.reader(ruttfile,delimiter=',')
    rutt=list(map(tuple,reader))
with open('res_cvru.txt') as cvrufile:#[|cv|type|ru|]
    reader=csv.reader(cvrufile,delimiter=',')
    cvru=list(map(tuple,reader))
d1=[]
for x in range(1,len(ttru)):#
    for j in range(1,len(rucv)):##normalize(ttru[1][1]).lower()
        if str(ttru[x][3]).lower()==str(rucv[j][3][:len(rucv[j][3])-1]).lower():
            #print(ttru[x][3]+'='+rucv[j][3][:len(rucv[j][3])-1])
            s=normalize(ttru[x][1][:len(ttru[x][1])-1]).lower()+':'+normalize(ttru[x][2]).lower()+'.'+normalize(rucv[j][2]).lower()+':'+normalize(rucv[j][1]).lower()+':'+str(ttru[x][3]).lower()
            d1.append(s.lower())
    if x%250==0:
        print('d '+str(len(d1)))
###
dunic1=['test']
x=len(d1)-1
flag='netu'
while x!=-1:
    for y in range(len(dunic1)):
        if d1[x]==dunic1[y]:
            flag='yest'
            break
    if flag=='netu':
        dunic1.append(str(d1[x]))
    if flag=='yest':
        flag='netu'
    d1.pop(x)
    x-=1
###
fil1=open('rezult11.txt','w')
for x in range(len(dunic1)):
    fil1.write(dunic1[x]+'\n')#ballnaya syatema
fil1.close()
d2=[]
for x in range(1,len(rutt)):#
    for j in range(1,len(cvru)):##normalize(ttru[1][1]).lower()
        if str(rutt[x][3][:len(rutt[x][3])-1]).lower()==str(cvru[j][3]).lower():
            #print(ttru[x][3]+'='+rucv[j][3][:len(rucv[j][3])-1])
            fff=open('bug.txt','w')
            fff.write(rutt[x][1]+rutt[x][2]+rutt[x][3]+'\n')
            fff.write(rutt[x+1][1]+rutt[x+1][2]+rutt[x+1][3]+'\n')
            fff.write(cvru[j][1]+cvru[j][2]+cvru[j][3]+'\n')
            fff.write(cvru[j+1][1]+cvru[j+1][2]+cvru[j+1][3]+'\n')
            fff.close()
            #print(rutt[x][1]+rutt[x][2]+rutt[x][3])
            p1=normalize(rutt[x][1]).lower()
            p2=normalize(rutt[x][2]).lower()
            p3=normalize(cvru[j][2]).lower()
            p4=normalize(cvru[j][1][:len(cvru[j][1])-1]).lower()
            s=p1+':'+p2+'.'+p3+':'+p4+':'+str(rutt[x][3][:len(rutt[x][3])-1]).lower()
            d2.append(s.lower())
    if x%250==0:
        print('d '+str(len(d2)))

###
dunic1=[]
dunic2=['test']
x=len(d2)-1
flag='netu'
while x!=-1:
    for y in range(len(dunic2)):
        if d2[x]==dunic2[y]:
            flag='yest'
            break
    if flag=='netu':
        dunic2.append(str(d2[x]))
    if flag=='yest':
        flag='netu'
    d2.pop(x)
    x-=1
###
fil2=open('rezult22.txt','w')
for x in range(len(dunic2)):
    fil2.write(dunic2[x]+'\n')#ballnaya syatema
fil2.close()
###
print('DONE')
input()
#for x in range(len(l)):
#    print(l[x][3])
