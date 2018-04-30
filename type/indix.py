# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
#numerals <e><p><l>пӗрре<s n="num"/></l><r>бер<s n="num"/></r></p></e>
#pronouns <e><p><l>вӗсем<s n="prn"/><s n="pers"/></l><r>алар<s n="prn"/><s n="pers"/></r></p></e>
###nouns <e><p><l>ум<s n="n"/></l><r>алд<s n="n"/></r></p></e>
#verbs  <e><p><l>пул<s n="v"/><s n="iv"/></l><r>бул<s n="v"/><s n="iv"/></r></p></e>
#imena sobstv <e><p><l>Ахмет<s n="np"/></l><r>Әхмәт<s n="np"/></r></p></e>
#adjectives <e><p><l>пур<s n="adj"/></l><r>бар<s n="adj"/></r></p></e>
#adverbs <e><p><l>ӑҫта<s n="adv"/><s n="itg"/></l><r>кайда<s n="adv"/><s n="itg"/></r></p></e>
def todix(name,param):
    prev=''
    first=''
    fin=open(name,'r')
    fout=open('normalized/'+name[:len(name)-3]+'dix','w')
    for line in fin:#fin:
        s=line.split(':')#<e><p><l>ум<s n="n"/></l><r>алд<s n="n"/></r></p></e>
        #for x in range(len(s)):
        #    s[x]=normalize(str(s[x])).lower()
        if str(s[0])==prev and first==str(s[2]):
            continue
        if prev=='':
            prev=str(s[0])
            first=str(s[2])
        if prev!=str(s[0]):
            result='<e><p><l>'+str(s[2][:len(str(s[2]))-1])+'<s n="'+param+'"/></l><r>'+str(s[0])+'<s n="'+param+'"/></r></p></e>'+'\n'
        if prev==str(s[0]):
            result='<e r="LR"><p><l>'+str(s[2][:len(str(s[2]))-1])+'<s n="'+param+'"/></l><r>'+str(s[0])+'<s n="'+param+'"/></r></p></e>'+'\n'
        
        fout.write(result)
        prev=str(s[0])
    fout.close()
    fin.close()
        #time.sleep(100)
    #input()

todix('noun\'s.txt','n')
todix('adjective\'s.txt','adj')
todix('adverb\'s.txt','adv')
todix('verb\'s.txt','v')
todix('propername\'s.txt','np')
todix('pronoun\'s.txt','pn')
todix('numeral\'s.txt','num')
print('allo')
    
