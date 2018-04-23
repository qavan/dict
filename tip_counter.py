import time
def tom(f1):
    global LIST
    for line in f1:
        LIST.append(line[:len(line)-1])
tip=[['type1','type2','0']]
LIST=[]
f=open('type/ostatok.txt','r')
tom(f)
f.close()
print(len(LIST))

for x in range(len(LIST)):
    flag=False
    s=str(LIST[x]).split('-')
    d=s[1].split('.')#d[0] d[1]
    #print(d[0])
    #print(d[1])
    #if x%100==0:
    #print('x='+str(x))
    for i in range(len(tip)):
        #print('i='+str(i))
        #print(str(i)+d[0]+'||'+d[1])
        #print(str(x)+tip[i][0]+' '+tip[i][1])
        if (d[0]==tip[i][0] and d[1]==tip[i][1]) or (d[0]==tip[i][1] and d[1]==tip[i][0]):
            tip[i][2]=int(tip[i][2])+1
            flag=True
            #print('exit')
            break
    if  flag==False:
        p=[]
        p.append(d[0])
        p.append(d[1])
        p.append('0')
        #print(p)
        tip.append(p)
        flag=False
#tip.sort()
fil=open('type/tipu.txt','w')
for j in range(len(tip)):
    fil.write(str(tip[j])+'\n')
fil.close()

print(len(tip))
    
    
