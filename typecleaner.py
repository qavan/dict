import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
f=open('rezult11.txt','r')
warriors=open('type/warriors.txt','w')
#e=open('type/e\'s.txt','w')
nouns=open('type/noun\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
#e=open('type/e\'s.txt','w')
dc=[]
i=0
ost=open('ostatok.txt','w')
for line in f:
    i+=1
    s=line[:len(line)-1]
    d=s.split('-')
    bug=open('bug.txt','w')
    bug.write(line)
    bug.close()
    if len(d)==3:
        tt=d[0]
        cv=d[2]
        types=str(d[1]).split('.')
        if str(types[0])==str(types[1]) and str(types[0])=='noun':
            nouns.write(normalize(tt)+':'+types[0]+':'+normalize(cv)+'\n')
        else:
            ost.write(line)            
    else:
        dc.append(line)
    #r=str(input())
    #if r=='2':
    #    break
    if i==13063:
        break
slash=open('type/defis.txt','w')
for x in range(len(dc)):
    slash.write(dc[x])
slash.close()
nouns.close()
ost.close()
print('DONE')

