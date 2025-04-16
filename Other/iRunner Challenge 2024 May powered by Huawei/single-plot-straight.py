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
    
    distances += [np.abs(line(points[0][0], points[0][1])) / np.sqrt(nor[0] ** 2 + nor[1] ** 2)]

    xi = points[0][0] - sign(line(points[0][0], points[0][1])) * distances[-1] * nor[0] / veclen(nor)
    yi = points[0][1] - sign(line(points[0][0], points[0][1])) * distances[-1] * nor[1] / veclen(nor)
    M = np.array([xi, yi])                                          # Ближайшая точка прямой к заданной точке
    
                                                                    # Если точка на отрезке, то возвращаем её, иначе одну из вершин
    if ((vertices[i] <= M)[0] == (M <= vertices[i+1])[0] and (vertices[i] <= M)[1] == (M <= vertices[i+1])[1]): intersections += [np.array([xi,yi])]
    elif veclen(vertices[i] - points[0]) > veclen(vertices[i+1] - points[0]): 
        intersections += [vertices[i+1]]
        distances[-1] = veclen(vertices[i+1] - points[0])
    else:
        intersections += [vertices[i]]
        distances[-1] = veclen(vertices[i] - points[0])

intersections = np.array(intersections)
mindist = min(distances)
minpoint = intersections[np.where(distances == mindist)[0]][0]
print("Min distance is: ", mindist, " and nearest point is: ", minpoint)



crosses = 0
if mindist == 0:                                                    # Если лежит на отрезке
    crosses = 1
else:
    for i in range(len(vertices) - 1):
        vec = vertices[i + 1] - vertices[i]
        nor = np.dot( np.array([0, -1, 1, 0]).reshape(2,2), vec )
        c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
                                                                    # Иначе строим прямую параллельную X
        
        x0 = points[0][0]
        y0 = points[0][1]
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
d = mindist**2 * (-1 if crosses % 2 == 0 else 1)                    # Проверка чётности и нечётности кол-ва пересечений
print("Answer is: ", d, minpoint)



fig = plt.figure()                                                  # Отрисовка графика
plt.axis("equal")
plt.plot(vertices[:,0], vertices[:,1])
plt.plot(points[:,0], points[:,1], 'ro', markersize=1)
plt.plot([minpoint[0], points[0,0]], [minpoint[1], points[0,1]], 'go')
plt.show()