import sys
import time

start = time.time()

word = sys.argv[2]

f = open(sys.argv[1], 'r', encoding='utf8')                     # Файл
dictionary = list(f)

lineAlgStart = time.time()
lineAlg = []
i = 0
for line in dictionary:
    if word == line.replace('\n',''):                           # Ввод и обработка 1ым способом
        while i < len(dictionary) and dictionary[i][:len(word)] == word:
            lineAlg.append(dictionary[i].replace('\n',''))
            i += 1
        break
    i += 1
lineAlgTime = time.time() - lineAlgStart

f.seek(0)                                                       # Ещё раз читаем файл

binarAlgStart = time.time()
binarAlg = []
low = 0
high = len(dictionary) - 1
while low <= high:
    mid = (low + high) // 2

    if word == dictionary[mid].replace('\n',''):
        i = mid                                                 # Ввод и обработка вторым способом
        while i < len(dictionary) and dictionary[i][:len(word)] == word:
            binarAlg.append(dictionary[i].replace('\n',''))
            i += 1
        break
    
    if word > dictionary[mid]: low = mid + 1
    else: high = mid - 1
binarAlgTime = time.time() - binarAlgStart



f.close()

print(lineAlg)
print(lineAlgTime)                                              # Вывод
print(binarAlg)
print(binarAlgTime)

# print(f'All time is {time.time() - start}')