import numpy as np

n = int(input())
s = input()
vertices = np.array([float(i) for i in s.split()]).reshape(n, 2)
N = int(input())
points = []
for i in range(N):
    s = input()
    points.append([float(i) for i in s.split()])
points = np.array(points)
vertices = np.append(vertices, np.array([vertices[0]]), axis=0)
# return vertices, points