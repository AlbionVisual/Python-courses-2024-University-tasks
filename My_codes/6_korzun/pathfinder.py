from sys import argv as entries
from collections import deque
# import time

with open(entries[1], 'r', encoding='utf8') as f:
    a = tuple([int(i) for i in entries[2].split(',')])
    b = tuple([int(i) for i in entries[3].split(',')])
    table = []
    for line in f:
        table += [line.strip('\n')]

    height = len(table)
    width = len(table[0])

    graph = {}
    amount = 0
    for i in range(height):
        for j in range(width):
            if table[i][j] != '1':
                amount += 1
                graph[(i, j)] = []
                if i > 0 and table[i-1][j] != '1': graph[(i, j)] += [(i-1,j)]
                if j > 0 and table[i][j-1] != '1': graph[(i, j)] += [(i,j-1)]
                if i < height - 1 and table[i+1][j] != '1': graph[(i, j)] += [(i+1,j)]
                if j < width - 1 and table[i][j+1] != '1': graph[(i, j)] += [(i,j+1)]

    dists = {}
    dists[a] = 1
    Q = deque([a])
    res = 0
    matr = [[0] * width for i in range(height)]
    matr[a[0]][a[1]] = 1
    while Q and not res:
        el0 = Q.popleft()
        for eli in graph[el0]:
            if eli not in dists:
                dists[eli] = dists[el0] + 1
                matr[eli[0]][eli[1]] = dists[eli]
                if eli == b:
                    res = dists[eli]
                    break
                Q.append(eli)

    for line in matr:
        for el in line:
            print(f'{el:3d}', end = ' ')
        print()

    p = b
    path = [b]
    while p != a:
        dist_0 = matr[p[0]][p[1]]
        for cord in graph[p]:
            if matr[cord[0]][cord[1]] and matr[cord[0]][cord[1]] < dist_0:
                p = cord
                path += [p]
                break

        # if p[0] + 1 < len(matr) and dist_0 > matr[p[0] + 1][p[1]] and matr[p[0] + 1][p[1]]:
        #     p = (p[0] + 1, p[1])
        # elif p[1] + 1 < len(matr[0]) and dist_0 > matr[p[0]][p[1] + 1] and matr[p[0]][p[1] + 1]:
        #     p = (p[0], p[1] + 1)
        # elif p[0] > 0 and dist_0 > matr[p[0] - 1][p[1]] and matr[p[0] - 1][p[1]]:
        #     p = (p[0] - 1, p[1])
        # elif p[1] > 0 and dist_0 > matr[p[0]][p[1] - 1] and matr[p[0]][p[1] - 1]:
        #     p = (p[0], p[1] - 1)
        # path += [p]
    
    print(list(reversed(path)))