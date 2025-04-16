import sys, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

freqs = []
xchanges = []
ychanges = []                                       # Создание

with open(sys.argv[1], 'r', encoding='utf8') as f:
    freqs = [float(i) for i in f.readline().split()]
    f.readline()
    line = f.readline()                             # Чтение и обработка
    while line != '\n':
        xchanges.append([float(i) for i in line.split()])
        line = f.readline()

    for line in f:
        ychanges.append([float(i) for i in line.split()])

def init():
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.19, 1.01)
    return ln,

def animate(i):                                     # Ф-ция для изменения кадров
    r = random.random()
    i = 0
    while sum(freqs[:i]) < r:
        i += 1
    i -= 1

    x.append(x[-1] * xchanges[i][0] + y[-1] * xchanges[i][1] + xchanges[i][2])
    y.append(x[-2] * ychanges[i][0] + y[-1] * ychanges[i][1] + ychanges[i][2])
    ln.set_data(x, y)
    return ln,

fig, ax = plt.subplots()
x, y = [0], [0]
ln, = plt.plot(x, y, 'bo', markersize=1)
                                                    # Вывод анимации
ani = FuncAnimation(fig, animate, init_func=init, interval=0.01)
plt.show()