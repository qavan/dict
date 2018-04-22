import csv
import pandas as pd
import re
def normalize(x):
    stroka=re.sub(r'[\000-\377]*', lambda m:''.join([chr(ord(i)) for i in m.group(0)]).decode('utf8'),x)
    return stroka
def csvr(f):
    """
    Read a CSV file using csv.DictReader
    """
    reader=csv.DictReader(f,delimiter=',')
    for line in reader:
        s=line["tt"]+line["type"]+' '+line["ru"]
        s=s.split(' ')
        s=' '.join(s)
        print(s)
        input()
with open('res_ttru.txt') as ttrufile:#[|tt|type|ru|]
    reader=csv.reader(ttrufile,delimiter=',')
    ttru=list(map(tuple,reader))
with open('res_rucv.txt') as rucvfile:#[|cv|type|ru|]
    reader=csv.reader(rucvfile,delimiter=',')
    rucv=list(map(tuple,reader))
with open('res_rutt.txt') as ruttfile:#[|tt|type|ru|]
    reader=csv.reader(ruttfile,delimiter=',')
    rutt=list(map(tuple,reader))
with open('res_cvru.txt') as cvrufile:#[|cv|type|ru|]
    reader=csv.reader(cvrufile,delimiter=',')
    cvru=list(map(tuple,reader))
d=[]
print(normalize(ttru[1][1]))
print(normalize(ttru[1][1]).lower())
