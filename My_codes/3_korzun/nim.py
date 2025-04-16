import sys

def nimSum(arr):                                    # Подсчёт ним-суммы
    s = arr[0]
    for i in range(1, len(arr)):
        s = s ^ arr[i]
    return s

def max(arr):                                       # Поиск индекса максимального элемента
    biggest = 0
    for i in range(len(arr)):
            if arr[biggest] < arr[i]:
                biggest = i
    return biggest

turn = int(sys.argv[1])
amounts = [int(i) for i in sys.argv[2].split()]     # Инициализация
space = ' '

n = len(amounts)

while sum(amounts) != 0:                            # Пока игра идёт
    if turn:                                        # Ходит игрок
        
        ans = [int(i) for i in input(f'Borad: {space.join([str(i) for i in amounts])}. Your turn. Enter pile and number of stones: ').split()]
        amounts[ans[0] - 1] -= ans[1]
        if amounts[ans[0] - 1] < 0: amounts[ans[0] - 1] = 0
    else:                                           # Ходит компьютер
        
        temp = amounts[:]
        biggest = max(temp)                         # Компьютер пытается походить наилучшим образом
        
        temp[biggest] -= 1
        while nimSum(temp) and temp[biggest] > 0: temp[biggest] -= 1

        print((f'Borad: {space.join([str(i) for i in amounts])}. My turn: {biggest + 1} {amounts[biggest] - temp[biggest]}'))
        amounts = temp[:]

    turn = not turn

if turn: print('I won!')
else: print('You won!')                             # Конец игры