import matplotlib.pyplot as plt
import timeit

def getCells(radius, x0 = 0, y0 = 0, depth = 6):
    preva = 1 # cos or with x
    prevb = 0 # sin or for y
    size = 128
    p1 = (-size/2, -size/2)
    cellsize = size / 2**depth
    cells = []
    phase = 0
    loops = 0
    while not loops:
        if abs(preva) >= 2**.5 / 2:
            if preva > 0:
                if phase != 0 and prevb >= 0:
                    phase = 0
                    loops += 1
                    break
                b = cellsize / radius + prevb
                a = (1 - b**2)**.5
            else:
                b = prevb - cellsize / radius
                a = -(1 - b**2)**.5
                phase = 2
        else:
            if prevb > 0:
                a = preva - cellsize / radius
                b = (1 - a**2)**.5
                phase = 1
            else:
                a = cellsize / radius + preva
                b = -(1 - a**2)**.5
                phase = 3
            
        preva = a
        prevb = b
        point = (x0 + a*radius, y0 + b*radius)
        cell = (int((point[0] - p1[0]) * 2**depth // size), int((point[1] - p1[1]) * 2**depth // size))
        if cell[0] >= 0 and cell[1] >= 0 and cell[0] < 2**depth and cell[1] < 2**depth: cells += [cell]    
    return cells
cells = [],[]

def call():
    global cells
    cells = getCells(2, 15,14)
time = timeit.timeit(call, number = 100) / 100

for i in range(len(cells)):
    print(cells[i])
print(len(cells))

xarr = [val[0] for val in cells]
yarr = [val[1] for val in cells]

plt.axis("equal")
plt.plot(xarr, yarr, 'bo')
plt.grid(True)
plt.show()

print(time)