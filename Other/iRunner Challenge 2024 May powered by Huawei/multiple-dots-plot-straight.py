import matplotlib.pyplot as plt
import numpy as np
from sys import argv as entries

# entries = [1, "./iRunner Challenge 2024 May powered by Huawei/one-figure-test.txt"]
f = open(entries[1], 'r', encoding='utf8')                          # Ввод информации
t = f.readline()
n = int(f.readline().strip('\n'))
s = f.readline().strip('\n')
vertices = np.array([float(i) for i in s.split()]).reshape(n, 2)
N = int(f.readline().strip('\n'))
points = []
for i in range(N):
    s = f.readline().strip('\n')
    points.append([float(i) for i in s.split()])
points = np.array(points)
vertices = np.append(vertices, np.array([vertices[0]]), axis=0)

def min(obj):
    ind = 0
    for i in range(1, len(obj)):
        if obj[i] < obj[ind]: ind = i
    return obj[ind], ind

sign = lambda x: x / np.abs(x) if x != 0 else 0                     # Подсчёт минимального расстояния
veclen = lambda v: np.sqrt(v[0] ** 2 + v[1] ** 2)
distances = []
intersections = []
for i in range(len(vertices) - 1):
    vec = vertices[i + 1] - vertices[i]                             # Вектор от двух вершин
    nor = np.dot( np.array([0, -1, 1, 0]).reshape(2,2), vec )       # Нормальный вектор
    # line: ax + by + c = 0
    c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
    line = lambda x, y: nor[0] * x + nor[1] * y + c                 # Левая часть уравнения прямой
    distances.append([])
    intersections.append([])
    for point in points:
        distances[-1] += [np.abs(line(point[0], point[1])) / np.sqrt(nor[0] ** 2 + nor[1] ** 2)]

        xi = point[0] - sign(line(point[0], point[1])) * distances[-1][-1] * nor[0] / veclen(nor)
        yi = point[1] - sign(line(point[0], point[1])) * distances[-1][-1] * nor[1] / veclen(nor)
        M = np.array([xi, yi])                                          # Ближайшая точка прямой к заданной точке
        
                                                                        # Если точка на отрезке, то возвращаем её, иначе одну из вершин
        if ((vertices[i] <= M)[0] == (M <= vertices[i+1])[0] and (vertices[i] <= M)[1] == (M <= vertices[i+1])[1]): intersections[-1] += [np.array([xi,yi])]
        elif veclen(vertices[i] - point) > veclen(vertices[i+1] - point): 
            intersections[-1] += [vertices[i+1]]
            distances[-1][-1] = veclen(vertices[i+1] - point)
        else:
            intersections[-1] += [vertices[i]]
            distances[-1][-1] = veclen(vertices[i] - point)

mindists = []
distances = np.transpose(np.array([np.array(d) for d in distances]))
intersections = np.transpose(np.array([np.array(i) for i in intersections]), (1,0,2))
minpoints = []
for i in range(len(distances)):
    # print("Adding point: ", i)
    intersections[i] = np.array(intersections[i])
    mindist, minind = min(distances[i])
    mindists += [mindist]
    minpoints += [np.array(intersections[i][minind])]
    # print("Min distance is: ", mindist, " and nearest point is: ", minpoint)

f = open('answers.txt', 'w', encoding='utf8')
for j in range(len(points)):
    crosses = 0
    if mindists[j] == 0:                                                    # Если лежит на отрезке
        crosses = 1
    else:
        for i in range(len(vertices) - 1):
            vec = vertices[i + 1] - vertices[i]
            nor = np.dot( np.array([0, -1, 1, 0]).reshape(2,2), vec )
            c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
                                                                        # Иначе строим прямую параллельную X
            
            x0 = points[j][0]
            y0 = points[j][1]
            # abs(vertices[prev][1] - y0) < 1e-6 != abs(vertices[next][1] - y0) < 1e-6 # Пример приблизительного сравнения, понадобится в случае интересной точности питона
            if nor[0] == 0:                                             # Ипроверяем условия
                if nor[1] * y0 == - c:                                  # Если полученная прямая вкладывает в себя отрезок
                    prev = i - 1 if i != 0 else n - 1; next = i + 2
                    if (vertices[prev][1] > y0) != (vertices[next][1] > y0) and vertices[next][0] > x0:
                        crosses += 1                                    # То добавляем к кол-ву 1 только в случае, если предыдущая и следующая точки лежат по разные стороны от нашей прямой
            else:
                xi = (-c-nor[1]*y0) / nor[0]                            # x-координата пересечения прямой с прямой образованной стороной
                if i == len(vertices) - 2 and xi > x0 and xi == vertices[i+1][0] and y0 == vertices[i+1][1]:    # Далее идут два условия, проверяющие если точки пересекаются нашей прямой
                    prev = i; next = 0                                  # Первое условие проверяется только в конце, для проверки последней точки   
                    if (vertices[prev][1] > y0) != (vertices[next][1] > y0) and vertices[prev][1] != y0 and vertices[next][1] != y0:
                        crosses += 1                                    # Алгоритм такой же как и в первом условии и следующем
                elif xi > x0 and xi == vertices[i][0] and y0 == vertices[i][1]:     # Проверяет совпадение всех точек кроме последней
                    prev = i - 1 if i != 0 else n - 1; next = i+1
                    if (vertices[prev][1] > y0) != (vertices[next][1] > y0) and vertices[prev][1] != y0 and vertices[next][1] != y0:
                        crosses += 1                                    # В случае совпадения проверяет: если предыдущая и следующая точки лежат по разные стороны от прямой, то добавить 1 иначе ничего
                elif xi > x0 and (vertices[i+1][1] > y0) == (vertices[i][1] < y0) and vertices[i+1][1] != y0 and vertices[i][1] != y0:
                    crosses += 1                                        # Заглушка или случай простого пересечения отрезка с прямой
            # print(crosses)
                                                                        # !!! Все условия проверяют: лежит ли точка пересечения на отрезке или за ним, координата x пересечения больше координаты данной точки
    d = mindists[j]**2 * (-1 if crosses % 2 == 0 else 1)                    # Проверка чётности и нечётности кол-ва пересечений
    print(f'{j}: {d}, x: {minpoints[j][0]}, y: {minpoints[j][1]}')
    f.write(str(round(d, 8)) + ' ' + str(round(minpoints[j][0], 8)) + ' ' + str(round(minpoints[j][1], 8)) + '\n')

f.close()

minpoints = np.array(minpoints)
# print(minpoints)
# print(points)
# print((minpoints + points)[:,0])

fig = plt.figure()                                                  # Отрисовка графика
plt.axis("equal")
plt.plot(vertices[:,0], vertices[:,1])
plt.plot(points[:,0], points[:,1], 'ro', markersize=1)
plt.plot(minpoints[0,0], minpoints[0,1], 'go')
plt.show()