#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import re
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
def look():
    global tt,cv,types,count
    count+=1
    string=tt+':'+types[0]+':'+cv+'\n'#normalize( )
    return string
def t0():
    global types
    string=str(types[0])
    return string
def t1():
    global types
    string=str(types[1])
    return string
#----------
n=open('type/noun\'s.txt','w')
v=open('type/verb\'s.txt','w')
adv=open('type/adverb\'s.txt','w')
adj=open('type/adjective\'s.txt','w')
num=open('type/numeral\'s.txt','w')
prn=open('type/pronoun\'s.txt','w')
det=open('type/determiner\'s.txt','w')
pro=open('type/propername\'s.txt','w')
#e=open('type/e\'s.txt','w')
#---------
f1=open('rezult11.txt','r')
f2=open('rezult22.txt','r')
ost=open('type/ostatok.txt','w')
none=open('type/nonetype\'s.txt','w')
#---------
dc=[]
i=0
summ=0
count=0
tri=0
nnn=0
for line in f1:
    i+=1
    s=line[:len(line)-1]
    d=s.split('-')
   ##bug=open('bug.txt','w')
   ##bug.write(line)
   ##bug.close()
    if len(d)==3:
        tt=d[0]
        cv=d[2]
        types=str(d[1]).split('.')
        if t0()==t1() and t0()=='noun':#noun noun
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun') or (t1()=='nonetype' and t0()=='noun'):###########################################nonetype noun
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun feminine') or (t1()=='nonetype' and t0()=='noun feminine'):#########################nonetype noun feminine
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun masculine') or (t1()=='nonetype' and t0()=='noun masculine'):#######################nonetype noun masculine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun feminine') or (t1()=='noun' and t0()=='noun feminine'):#################################noun noun feminine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun masculine') or (t1()=='noun' and t0()=='noun masculine'):##############################noun noun masculine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun neuter') or (t1()=='noun' and t0()=='noun neuter'):#####################################noun noun neuter
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun neuter') or (t1()=='nonetype' and t0()=='noun neuter'):#############################nonetype noun neuter
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun p') or (t1()=='nonetype' and t0()=='noun p'):#######################################nonetype noun p
            n.write(look())
        elif (t0()=='noun' and t1()=='noun p') or (t1()=='noun' and t0()=='noun p'):###############################################noun noun p
            n.write(look())
        elif (t0()=='feminine' and t1()=='nonetype') or (t1()=='feminine' and t0()=='nonetype'):###################################feminine nonetype
            n.write(look())
        elif (t0()=='feminine' and t1()=='noun') or (t1()=='feminine' and t0()=='noun'):###########################################feminine noun
            n.write(look())
        elif (t0()=='neuter' and t1()=='noun') or (t1()=='neuter' and t0()=='noun'):###############################################neuter noun
            n.write(look())
        elif (t0()=='masculine' and t1()=='noun') or (t1()=='masculine' and t0()=='noun'):#########################################masculine noun
            n.write(look())
        elif (t0()=='noun particle' and t1()=='noun') or (t1()=='noun particle' and t0()=='noun'):#################################noun particle noun
            n.write(look())
        elif (t0()=='masculine' and t1()=='nonetype') or (t1()=='masculine' and t0()=='nonetype'):#################################masculine nonetype
            n.write(look())
        elif (t0()=='noun' and t1()=='proper masculine') or (t1()=='noun' and t0()=='proper masculine'):###########################noun proper masculine
            n.write(look())
         ###########
        elif t0()==t1() and t0()=='verb':##########################################################################################verb verb
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb') or (t1()=='nonetype' and t0()=='verb'):###########################################nonetype verb
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb pf') or (t1()=='nonetype' and t0()=='verb pf'):#####################################nonetype verb pf
            v.write(look())
        elif (t0()=='verb' and t1()=='verb pf') or (t1()=='verb' and t0()=='verb pf'):#############################################verb verb pf
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb impf') or (t1()=='nonetype' and t0()=='verb impf'):#################################nonetype verb impf
            v.write(look())
        elif (t0()=='verb' and t1()=='verb impf') or (t1()=='verb' and t0()=='verb impf'):#########################################verb verb impf
            v.write(look())
         ###########    
        elif t0()==t1() and t0()=='adverb':########################################################################################adverb adverb
            adv.write(look())
        elif (t0()=='nonetype' and t1()=='adverb') or (t1()=='nonetype' and t0()=='adverb'):#######################################nonetype adverb
            adv.write(look())###########
         ###########   
        elif t0()==t1() and t0()=='adjective':#####################################################################################adjective adjective
            adj.write(look())
        elif (t0()=='nonetype' and t1()=='adjective') or (t1()=='nonetype' and t0()=='adjective'):#################################nonetype adjective
            adj.write(look())
        elif (t0()=='nonetype' and t1()=='adjective masculine') or (t1()=='nonetype' and t0()=='adjective masculine'):#############nonetype adjective masculine 
            adj.write(look())
        elif (t0()=='adjective' and t1()=='adjective masculine') or (t1()=='adjective' and t0()=='adjective masculine'):###########adjective adjective masculine
            adj.write(look())
        elif (t0()=='adjective' and t1()=='noun masculine') or (t1()=='adjective' and t0()=='noun masculine'):#####################adjective noun masculine
            adj.write(look())
        #$elif (t0()=='nonetype' and t1()=='adjective noun') or (t1()=='nonetype' and t0()=='adjective noun'):######################nonetype adjective noun 
        #$    adj.write(look())
          ###########  
        elif t0()==t1() and t0()=='numeral':#######################################################################################numeral numeral
            num.write(look())
        elif (t0()=='nonetype' and t1()=='numeral') or (t1()=='nonetype' and t0()=='numeral'):#####################################nonetype numeral
            num.write(look())
        elif (t0()=='determiner' and t1()=='numeral') or (t1()=='determiner' and t0()=='numeral'):#################################determiner numeral
            num.write(look())
        elif (t0()=='number' and t1()=='numeral') or (t1()=='number' and t0()=='numeral'):#########################################number numeral
            num.write(look())
          ###########  
        elif t0()==t1() and t0()=='pronoun':#######################################################################################pronoun pronoun
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun') or (t1()=='nonetype' and t0()=='pronoun'):#####################################nonetype pronoun
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun neuter') or (t1()=='nonetype' and t0()=='pronoun neuter'):#######################nonetype pronoun neuter
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun masculine') or (t1()=='nonetype' and t0()=='pronoun masculine'):#################onetype ppronoun masculine
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun p') or (t1()=='nonetype' and t0()=='pronoun p'):#################################nonetype pronoun p
            prn.write(look())
          ###########
        elif (t0()=='nonetype' and t1()=='proper masculine') or (t1()=='nonetype' and t0()=='proper masculine'):###################nonetype proper masculine
            pro.write(look())
        elif (t0()=='nonetype' and t1()=='proper') or (t1()=='nonetype' and t0()=='proper'):#######################################nonetype proper
            pro.write(look())
        elif (t0()=='nonetype' and t1()=='proper feminine') or (t1()=='nonetype' and t0()=='proper feminine'):#####################nonetype proper feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='proper feminine') or (t1()=='proper' and t0()=='proper feminine'):#########################proper proper feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='proper masculine') or (t1()=='proper' and t0()=='proper masculine'):#######################proper proper masculine
            pro.write(look())
        elif (t0()=='proper neuter' and t1()=='nonetype') or (t1()=='proper neuter' and t0()=='nonetype'):#########################proper neuter proper masculine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun feminine') or (t1()=='proper' and t0()=='noun feminine'):#############################proper noun feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun masculine') or (t1()=='proper' and t0()=='noun masculine'):###########################proper noun masculine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun') or (t1()=='proper' and t0()=='noun'):###############################################proper noun
            pro.write(look())
          ###########
        elif t0()==t1() and t0()=='determiner':####################################################################################determiner determiner
            det.write(look())
        elif (t0()=='nonetype' and t1()=='determiner') or (t1()=='nonetype' and t0()=='determiner'):###############################nonetype determiner
            det.write(look())
        elif (t0()=='nonetype' and t1()=='determiner feminine') or (t1()=='nonetype' and t0()=='determiner feminine'):#############nonetype determiner feminine
            det.write(look())
        ###-------------------###
        ###-------------------###
        elif (t0()=='noun' and t1()=='adjective') or (t1()=='noun' and t0()=='adjective'):#########################################noun adjective
            n.write(look())
            adj.write(look())
        elif (t0()=='adverb' and t1()=='adjective') or (t1()=='adverb' and t0()=='adjective'):######################################adverb adjective
            adv.write(look())
            adj.write(look())                 
        elif (t0()=='nonetype' and t1()=='adjective adverb') or (t1()=='nonetype' and t0()=='adjective adverb'):###################nonetype adjective adverb
            adj.write(look())
            adv.write(look())
        elif (t0()=='adjective' and t1()=='adjective adverb') or (t1()=='adjective' and t0()=='adjective adverb'):##################adjective adjective adverb
            adj.write(look())
            adv.write(look())
        ###-------------------###
        ###-------------------###
            ############################

            
        elif t0()=='nonetype' and t1()=='nonetype':
            nnn+=1
            count-=1
            none.write(look())
        else:
            tri+=1
            ost.write(line)
    else:
        summ+=1
        dc.append(line)
    if i==13056:
        print('rezult11.####### '+str(i))
        break
for line in f2:
    i+=1
    s=line[:len(line)-1]
    d=s.split('-')
   ##bug=open('debug.txt','w')
   ##bug.write(line)
   ##bug.close()
    if len(d)==3:
        tt=d[0]
        cv=d[2]
        types=str(d[1]).split('.')
        if t0()==t1() and t0()=='noun':#noun noun
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun') or (t1()=='nonetype' and t0()=='noun'):###########################################nonetype noun
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun feminine') or (t1()=='nonetype' and t0()=='noun feminine'):#########################nonetype noun feminine
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun masculine') or (t1()=='nonetype' and t0()=='noun masculine'):#######################nonetype noun masculine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun feminine') or (t1()=='noun' and t0()=='noun feminine'):#################################noun noun feminine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun masculine') or (t1()=='noun' and t0()=='noun masculine'):##############################noun noun masculine
            n.write(look())
        elif (t0()=='noun' and t1()=='noun neuter') or (t1()=='noun' and t0()=='noun neuter'):#####################################noun noun neuter
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun neuter') or (t1()=='nonetype' and t0()=='noun neuter'):#############################nonetype noun neuter
            n.write(look())
        elif (t0()=='nonetype' and t1()=='noun p') or (t1()=='nonetype' and t0()=='noun p'):#######################################nonetype noun p
            n.write(look())
        elif (t0()=='noun' and t1()=='noun p') or (t1()=='noun' and t0()=='noun p'):###############################################noun noun p
            n.write(look())
        elif (t0()=='feminine' and t1()=='nonetype') or (t1()=='feminine' and t0()=='nonetype'):###################################feminine nonetype
            n.write(look())
        elif (t0()=='feminine' and t1()=='noun') or (t1()=='feminine' and t0()=='noun'):###########################################feminine noun
            n.write(look())
        elif (t0()=='neuter' and t1()=='noun') or (t1()=='neuter' and t0()=='noun'):###############################################neuter noun
            n.write(look())
        elif (t0()=='masculine' and t1()=='noun') or (t1()=='masculine' and t0()=='noun'):#########################################masculine noun
            n.write(look())
        elif (t0()=='noun particle' and t1()=='noun') or (t1()=='noun particle' and t0()=='noun'):#################################noun particle noun
            n.write(look())
        elif (t0()=='masculine' and t1()=='nonetype') or (t1()=='masculine' and t0()=='nonetype'):#################################masculine nonetype
            n.write(look())
        elif (t0()=='noun' and t1()=='proper masculine') or (t1()=='noun' and t0()=='proper masculine'):###########################noun proper masculine
            n.write(look())
         ###########
        elif t0()==t1() and t0()=='verb':##########################################################################################verb verb
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb') or (t1()=='nonetype' and t0()=='verb'):###########################################nonetype verb
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb pf') or (t1()=='nonetype' and t0()=='verb pf'):#####################################nonetype verb pf
            v.write(look())
        elif (t0()=='verb' and t1()=='verb pf') or (t1()=='verb' and t0()=='verb pf'):#############################################verb verb pf
            v.write(look())
        elif (t0()=='nonetype' and t1()=='verb impf') or (t1()=='nonetype' and t0()=='verb impf'):#################################nonetype verb impf
            v.write(look())
        elif (t0()=='verb' and t1()=='verb impf') or (t1()=='verb' and t0()=='verb impf'):#########################################verb verb impf
            v.write(look())
         ###########    
        elif t0()==t1() and t0()=='adverb':########################################################################################adverb adverb
            adv.write(look())
        elif (t0()=='nonetype' and t1()=='adverb') or (t1()=='nonetype' and t0()=='adverb'):#######################################nonetype adverb
            adv.write(look())###########
         ###########   
        elif t0()==t1() and t0()=='adjective':#####################################################################################adjective adjective
            adj.write(look())
        elif (t0()=='nonetype' and t1()=='adjective') or (t1()=='nonetype' and t0()=='adjective'):#################################nonetype adjective
            adj.write(look())
        elif (t0()=='nonetype' and t1()=='adjective masculine') or (t1()=='nonetype' and t0()=='adjective masculine'):#############nonetype adjective masculine 
            adj.write(look())
        elif (t0()=='adjective' and t1()=='adjective masculine') or (t1()=='adjective' and t0()=='adjective masculine'):###########adjective adjective masculine
            adj.write(look())
        elif (t0()=='adjective' and t1()=='noun masculine') or (t1()=='adjective' and t0()=='noun masculine'):#####################adjective noun masculine
            adj.write(look())
        #$elif (t0()=='nonetype' and t1()=='adjective noun') or (t1()=='nonetype' and t0()=='adjective noun'):######################nonetype adjective noun 
        #$    adj.write(look())
          ###########  
        elif t0()==t1() and t0()=='numeral':#######################################################################################numeral numeral
            num.write(look())
        elif (t0()=='nonetype' and t1()=='numeral') or (t1()=='nonetype' and t0()=='numeral'):#####################################nonetype numeral
            num.write(look())
        elif (t0()=='determiner' and t1()=='numeral') or (t1()=='determiner' and t0()=='numeral'):#################################determiner numeral
            num.write(look())
        elif (t0()=='number' and t1()=='numeral') or (t1()=='number' and t0()=='numeral'):#########################################number numeral
            num.write(look())
          ###########  
        elif t0()==t1() and t0()=='pronoun':#######################################################################################pronoun pronoun
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun') or (t1()=='nonetype' and t0()=='pronoun'):#####################################nonetype pronoun
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun neuter') or (t1()=='nonetype' and t0()=='pronoun neuter'):#######################nonetype pronoun neuter
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun masculine') or (t1()=='nonetype' and t0()=='pronoun masculine'):#################onetype ppronoun masculine
            prn.write(look())
        elif (t0()=='nonetype' and t1()=='pronoun p') or (t1()=='nonetype' and t0()=='pronoun p'):#################################nonetype pronoun p
            prn.write(look())
          ###########
        elif (t0()=='nonetype' and t1()=='proper masculine') or (t1()=='nonetype' and t0()=='proper masculine'):###################nonetype proper masculine
            pro.write(look())
        elif (t0()=='nonetype' and t1()=='proper') or (t1()=='nonetype' and t0()=='proper'):#######################################nonetype proper
            pro.write(look())
        elif (t0()=='nonetype' and t1()=='proper feminine') or (t1()=='nonetype' and t0()=='proper feminine'):#####################nonetype proper feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='proper feminine') or (t1()=='proper' and t0()=='proper feminine'):#########################proper proper feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='proper masculine') or (t1()=='proper' and t0()=='proper masculine'):#######################proper proper masculine
            pro.write(look())
        elif (t0()=='proper neuter' and t1()=='nonetype') or (t1()=='proper neuter' and t0()=='nonetype'):#########################proper neuter proper masculine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun feminine') or (t1()=='proper' and t0()=='noun feminine'):#############################proper noun feminine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun masculine') or (t1()=='proper' and t0()=='noun masculine'):###########################proper noun masculine
            pro.write(look())
        elif (t0()=='proper' and t1()=='noun') or (t1()=='proper' and t0()=='noun'):###############################################proper noun
            pro.write(look())
          ###########
        elif t0()==t1() and t0()=='determiner':####################################################################################determiner determiner
            det.write(look())
        elif (t0()=='nonetype' and t1()=='determiner') or (t1()=='nonetype' and t0()=='determiner'):###############################nonetype determiner
            det.write(look())
        elif (t0()=='nonetype' and t1()=='determiner feminine') or (t1()=='nonetype' and t0()=='determiner feminine'):#############nonetype determiner feminine
            det.write(look())
        ###-------------------###
        ###-------------------###
        elif (t0()=='noun' and t1()=='adjective') or (t1()=='noun' and t0()=='adjective'):#########################################noun adjective
            n.write(look())
            adj.write(look())
        elif (t0()=='adverb' and t1()=='adjective') or (t1()=='adverb' and t0()=='adjective'):######################################adverb adjective
            adv.write(look())
            adj.write(look())                 
        elif (t0()=='nonetype' and t1()=='adjective adverb') or (t1()=='nonetype' and t0()=='adjective adverb'):###################nonetype adjective adverb
            adj.write(look())
            adv.write(look())
        elif (t0()=='adjective' and t1()=='adjective adverb') or (t1()=='adjective' and t0()=='adjective adverb'):##################adjective adjective adverb
            adj.write(look())
            adv.write(look())
        ###-------------------###
        ###-------------------###
            ############################

            
        elif t0()=='nonetype' and t1()=='nonetype':
            nnn+=1
            count-=1
            none.write(look())
        else:
            tri+=1
            ost.write(line)
    else:
        summ+=1
        dc.append(line)
    if i==13056+15109:
        print('rezult22.####### '+str(i))
        break
f1.close()
f2.close()
ost.close()
defiserror=open('type/defis.txt','w')
print('- error########## '+str(summ))
print('pair\'s########## '+str(count))
print('other type\'s##### '+str(tri))
print('NONETYPE\'s####### '+str(nnn))
#input()
for x in range(len(dc)):
    defiserror.write(str(dc[x]))
defiserror.close()
n.close()
v.close()
adv.close()
adj.close()
num.close()
prn.close()
pro.close()
det.close()
none.close()
print('#######|ZAEBIS|#######')
input()
