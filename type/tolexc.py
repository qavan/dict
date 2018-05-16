import time
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
M=['noun']#,'verb','adverv','adjective','numeral','pronoun','determiner','propername']
fl=open('forfix.temp','r')
fs=fl.readline()
fs=fs.split(' ')

for line in fl:
    print(line)
    time.sleep(10)
for i in range(len(M)):
    if str(M[i])=='noun':
        tag='N'
    print(str(M[i])+'.txt')
    fin=open(str(M[i])+'.txt','r')
    fout=open('lexc/'+str(M[i])+'.temp','w')
    d=[]
    for line in fin:
        line=line.replace(str(fs[0]),str(fs[1]))
        line=line.replace(str(fs[2]),str(fs[3]))
        line=line.replace(str(fs[4]),str(fs[5]))
        line=line.replace(str(fs[6]),str(fs[7]))
        #time.sleep(10)

       
        s=line.split(':')
        d.append(str(s[2])+':'+str(s[2])+'                          '+tag+' ;          ! "'+str(s[3][:len(str(s[3]))-1])+'"'+'\n')
    #for x in range(len(d)):
    #    fout.write(str(d[x]))
    dunic=['test']
    x=len(d)-1
    flag='netu'
    while x!=-1:
        for y in range(len(dunic)):
            if d[x]==dunic[y]:
                flag='yest'
                break
        if flag=='netu':
            dunic.append(str(d[x]))
        if flag=='yest':
            flag='netu'
        d.pop(x)
        x-=1
    for x in range(len(dunic)):
        fout.write(str(dunic[x]))
    
fout.close()
