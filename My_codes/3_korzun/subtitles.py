import sys

def decodeTime(s):                                  # Переводит строку в кол-во секунд
    time = s.split(':')
    secs = int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])
    return secs

def encodeTime(s):                                  # Кодирует кол-во секунд в сртоку
    time = []
    time.append(str(int(s // 3600)).zfill(2))    
    s -= 3600 * (s // 3600)
    time.append(str(int(s // 60)).zfill(2))
    s -= 60 * (s // 60)
    time.append('{:06.3f}'.format(s))
    return ':'.join(time)

def addTime(s, time):                               # Основная ф-ция для изменения времени
    s = s.replace('\n', '').replace(',','.')
    times = s.split(' --> ')

    for i in range(2):
        times[i] = decodeTime(times[i])
        times[i] += time
        times[i] = encodeTime(times[i])
        times[i].replace('.',',')
        
    return f'{times[0]} --> {times[1]}'



f = open(sys.argv[1], 'r', encoding='utf8')
input = list(f)                                     # Ввод
f.close()

time = float(sys.argv[2])

output = []
for line in input:
    if "-->" in line:
        line = addTime(line, time)                  # Изменение
    output.append(line.replace('\n',''))

f = open(f'{sys.argv[1][:-4]}_updated.srt', 'x', encoding='utf8')
f.write('\n'.join(output))                          # Вывод
f.close()