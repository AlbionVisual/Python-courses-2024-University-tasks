import sys
import matplotlib.pyplot as plot
import random
# import time

# start = time.time()

def getWays(map, x, y):                                     # Выбор возможных путей
    n = len(map)
    ways = [False] * 4
    if x >= 1: ways[0] = not map[x - 1][y]
    if x < n - 1: ways[2] = not map[x + 1][y]
    if y >= 1: ways[3] = not map[x][y - 1]
    if y < n - 1: ways[1] = not map[x][y + 1]
    return ways
    

n = 20 if len(sys.argv) < 2 else int(sys.argv[1])

x = [int((n+1) / 2 + 0.5)]
y = [int((n+1) / 2 + 0.5)]
                                                            # Создание и инициализация переменных
ways = [True] * 4 # left top right bottom
turn = [[-1, 0], [0, 1], [1, 0], [0, -1]]
map = [[False] * n for i in range(n)]

turnNumber = 0

while sum(ways) != 0 and turnNumber < n**2:                 # Пока есть возможность куда-то ходить
    turnNumber += 1

    map[x[-1]][y[-1]] = True
    way = random.randint(0, sum(ways) - 1)                  # Ходим

    for i in range(4):
        if way == 0:
            if not ways[i]: continue
            x.append(x[-1] + turn[i][0])
            y.append(y[-1] + turn[i][1])
            break
        if ways[i]: way -= 1
        
    ways = getWays(map, x[-1], y[-1])                       # Смотрим возможные ходы


map[x[-1]][y[-1]] = False
for i in range(len(x)):
    x[i] += 1
    y[i] += 1

plot.plot(x, y)                                             # Х-ки графика
plot.plot([x[0]], [y[0]], 'ro')
plot.plot([x[-1]], [y[-1]], 'bo')
plot.xlim(1, n)
plot.ylim(1, n)
ticks = [x for x in range(1, n+1)]
plot.xticks(ticks)
plot.yticks(ticks)
plot.grid()

# print(time.time() - start)

plot.show()                                                 # Вывод графика