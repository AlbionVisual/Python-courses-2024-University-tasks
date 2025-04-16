from random import randrange
from random import random
import numpy as np
import sys

n = randrange(1, 2)
print("Amount of tests: ", n)
center = [randrange(-1000, 1000) for _ in range(2)]
sum1 = 0
sum2 = 0
with open(sys.argv[1],'w') as f:
    f.write(str(n)+"\n")
    for i in range(n):
        amount_vertex = randrange(3, 201)
        sum1 += amount_vertex
        # print("Amount of vertexes: ", amount_vertex)
        f.write(str(amount_vertex)+"\n")
        angles = np.linspace(0, 2*np.pi, amount_vertex)
        vec = np.array([1, 0])
        rot = lambda phi: np.array([np.array([np.cos(phi), -np.sin(phi)]), np.array([np.sin(phi), np.cos(phi)])])
        verticies=np.array([np.dot(rot(i), vec) * randrange(10, 5000) for i in angles])

        f.write(" ".join([str(round(i, 5)) for i in verticies.reshape(amount_vertex * 2)])+"\n")
        amount_dots = randrange(1,2)
        sum2 += amount_dots
        # print("Amount of dots: ", amount_dots)
        f.write(str(amount_dots)+"\n")
        for j in range(amount_dots):
            point = [str(round( -5000 + 10000 * random(), 5)) for i in range(2)]
            f.write(" ".join(point)+"\n")

print("Avg amount of vertecies is: ", round(sum1 / n, 3))
print("Avg amount of dots is: ", round(sum2 / n, 3))
