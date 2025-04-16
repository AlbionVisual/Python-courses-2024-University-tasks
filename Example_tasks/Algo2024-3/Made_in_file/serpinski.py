import sys, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cx = [0.0, 1.0, 0.5]
cy = [0.0, 0.0, 0.866]

fig, ax = plt.subplots()
fig.suptitle('Ковёр Серпинского')
x, y = [0], [0]
ln, = plt.plot(x, y, 'bo', markersize=1)

def init():
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1)
    return ln,

def animate(i):
    r = random.randrange(3)
    x.append((x[-1] + cx[r]) / 2.0)
    y.append((y[-1] + cy[r]) / 2.0)
    ln.set_data(x, y)
    return ln,

ani = FuncAnimation(fig, animate, init_func=init, interval=1)
plt.show()