from sys import argv as entries
from time import time

start = time()

file_in = entries[1]


fr = open(file_in, 'r', encoding='utf8')
amount = 0
dct = {}
s = 0
for line in fr:
    amount += 1
    s += len(line)
    sym = line[:1]
    if sym in dct:
        dct[sym] += 1
    else: dct[sym] = 1
avg = s / amount
fr.close()

lst = sorted([[dct[i], i] for i in dct.keys()], reverse=True)

deepness = 2
while lst[0][0] > amount / 4 and deepness < avg:
    fr = open(file_in, 'r', encoding='utf8')
    dct = {}
    for line in fr:
        sym = line[:deepness]
        if sym in dct:
            dct[sym] += 1
        else: dct[sym] = 1
    fr.close()
    deepness += 1
    lst = sorted([[dct[i], i] for i in dct.keys()], reverse=True)

fw = open('test.txt', 'w', encoding='utf8')
for el in lst:
    fw.write(str(el[1]) + ' -> ' + str(el[0]) + '\n')
fw.close()

print(time() - start)