from sys import argv as entries
from time import time
import tracemalloc

def merge_sort(arr, left, right):

    def merge(arr, left, right, mid):
        mid += 1
        right += 1
        arr1, arr2 = arr[left:mid], arr[mid:right]
        newarr = []
        if len(arr1) > len(arr2): arr1, arr2 = arr2, arr1
        id1 = id2 = 0
        while id1 + id2 < len(arr1) + len(arr2):
            if id2 >= len(arr2) or (id1 < len(arr1) and arr1[id1] < arr2[id2]): 
                newarr.append(arr1[id1])
                id1 += 1
            else: 
                newarr.append(arr2[id2])
                id2 += 1
        arr[left:right] = newarr
        return arr
    
    if (left < right):
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, right, mid)
        return arr
    return arr

def sort_line(s):
    line = s.strip('\n').split()
    return ' '.join(merge_sort(line, 0, len(line))) + '\n'

tracemalloc.start()
t0 = time()

# Первые чтение и анализ файла, записывает в искомый файл отсортированные строки:
file_in = entries[1]
file_out = entries[1][:-4] + '_out.txt'
fr = open(file_in, 'r', encoding='utf8')
fw = open(file_out, 'w', encoding='utf8')

amount = 0
s = 0
dct = {}
max = 0

for line in fr:
    amount += 1
    new = sort_line(line)
    sym = new[:1]
    if len(new) > max: max = len(new)
    if sym in dct:
        dct[sym]['amount'] += 1
        dct[sym]['pointers'] += [s]
    else: 
        dct[sym] = {'amount':1, 'pointers': [s]}
    s += len(new) + 1
    fw.write(new)
fr.close()
fw.close()
avg = s / amount

# Код на случай, если начала строк слишком много повторяются:
lst = sorted([[dct[i]['amount'], i] for i in dct.keys()], reverse=True)

deepness = 2
fr = open(file_out, 'r', encoding='utf8')
while lst[0][0] > amount / 4 and lst[0][1][-1] != '\n':
    fr.seek(0)
    dct = {}
    s = 0
    for line in fr:
        sym = line[:deepness]
        if sym in dct:
            dct[sym]['amount'] += 1
            dct[sym]['pointers'] += [s]
        else: 
            dct[sym] = {'amount':1, 'pointers': [s]}
        s += len(line) + 1
    
    deepness += 1
    lst = sorted([[dct[i]['amount'], i, dct[i]['pointers']] for i in dct.keys()], reverse=True)

# Не сортирует сами строки:
lst.sort(key=lambda x: x[1])

# #---------
# # Показывает насколько неразновидная в файле информация:
# if lst[0][1][-1] == '\n':
    # print('#dumbfile')

# # Можно посмотреть что в lst:
# fw = open('test_output.txt', 'w', encoding='utf8')
# for el in lst:
    # fw.write(str(el[1]) + ' -> ' + str(el[0]) + ' -> ' + str(el[2]) + '\n')
# fw.close()
# #---------

# Сортирует группы строк и добавляет их в конец искомого файла:
fr.seek(0)
fa = open(file_out, 'a', encoding='utf8')
fa.write('>SEPARATOR<\n')
for el in lst:
    # Это условие позволяет не записывать большую часть файла в переменную, если кол-во одинаковых строк превышает 40% всех строк
    if el[1][-1] == '\n':
        for i in range(el[0]):
            fa.write(el[1])
    else:
        to_sort = []
        for i in el[2]:
            fr.seek(i)
            to_sort.append(fr.readline())
        merge_sort(to_sort, 0, len(to_sort))
        for line in to_sort:
            fa.write(line)
fa.close()
fr.close()

# Удаление первой половины файла (не нашёл способа лучше без import os):
fr = open(file_out, 'r+b')
fr.seek(s)
fr.readline()
readpos = fr.tell()
writepos = 0
for i in range(amount):
    fr.seek(readpos)
    line = fr.readline()
    readpos = fr.tell()
    fr.seek(writepos)
    writepos += fr.write(line[:-2] + line[-1:])
fr.truncate(writepos - 1)
fr.close()

# Время и пиковая затрата памяти:
print(time()-t0, tracemalloc.get_traced_memory())
tracemalloc.stop()