import sys

output = []

f = open(sys.argv[1], 'r', encoding='utf8')
input = list(f)                                             # Ввод
f.close()
last = input[-1]                    # This four lines
input = [i[:-1] for i in input]     #
input.pop()                         # may be replaced with:
input.append(last)                  # input = [i.strip('\n') for i in input]
input.reverse()                                             # Переворачиваем для сохранения порядка

count = len(input)
for i in range(len(input)):
    if not input[i] in input[i+1:]:                         # Если элемент встречается дальше пропускаем его
        output.append(input[i])
        count -= 1                                          # Отнимаем от кол-ва элементов неудалённые = удалённые

output.reverse()

f = open(sys.argv[1], 'w', encoding='utf8')

f.write('\n'.join(output))                                  # Запись в файл
    
f.close()

print(count)                                                # Вывод