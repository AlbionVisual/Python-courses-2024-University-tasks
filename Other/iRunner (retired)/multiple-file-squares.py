import numpy as np
from sys import argv as entries
import time

# entries = [0, "iRunner Challenge 2024 May powered by Huawei/one-figure-test.txt"]

# def distPoint(side, point, dist):
#     xi = point[0] - sign(side["quo"](point[0], point[1])) * dist * side["nor"][0] / veclen(side["nor"])
#     yi = point[1] - sign(side["quo"](point[0], point[1])) * dist * side["nor"][1] / veclen(side["nor"])
#     return np.array([xi, yi])

# def calcNearest(sides, point):
#     distances = []
#     nearestPoints = []

#     for side in sides:
#         dist = calcDistance(side, point)
#         distances.append(dist)
#         nearestPoints.append(distPoint(side, point, dist))

#     mindist, ind = min(distances)
#     M = nearestPoints[ind]

#     if ((sides[ind]["p1"] <= M)[0] == (M <= sides[ind]["p2"])[0] and (sides[ind]["p1"] <= M)[1] == (M <= sides[ind]["p2"])[1]):
#         return mindist**2, M
#     elif sqrlen(sides[ind]["p1"] - point) > sqrlen(sides[ind]["p2"] - point):  
#         return sqrlen(sides[ind]["p2"] - point), sides[ind]["p2"]
#     else: 
#         return sqrlen(sides[ind]["p1"] - point), sides[ind]["p1"]

def sign(c):
    return 1 if c > 0 else -1 if c < 0 else 0

def sqrlen(vec):
    return vec[0]**2 + vec[1]**2

def veclen(vec):
    return np.sqrt(vec[0]**2 + vec[1]**2)

def min(obj):
    ind = 0
    for i in range(1, len(obj)):
        if obj[i] < obj[ind]: ind = i
    return obj[ind], ind

def calcDistance(side, point):
    return np.abs(side["quo"](point[0], point[1])) / veclen(side["nor"])

def readTest(f):
    n = int(f.readline().strip('\n'))
    s = f.readline().strip('\n')
    vertices = np.array([float(i) for i in s.split()]).reshape(n, 2)
    N = int(f.readline().strip('\n'))
    points = []
    for _ in range(N):
        s = f.readline().strip('\n')
        points.append([float(i) for i in s.split()])
    points = np.array(points)
    vertices = np.append(vertices, np.array([vertices[0]]), axis=0)
    return vertices, points

def calcStartSquare(points):
    minx, miny = points[0]
    maxx, maxy = points[0]
    for point in points:
        if point[0] > maxx: maxx = point[0]
        if point[1] > maxy: maxy = point[1]
        if point[0] < minx: minx = point[0]
        if point[1] < miny: miny = point[1]
    if maxx - minx < maxy - miny:
        maxx = minx + maxy - miny
    else:
        maxy = miny + maxx - minx
    size = maxx - minx
    return [[minx - size * 1e-5, miny - size * 1e-5],[maxx + size * 1e-5, maxy + size * 1e-5]]

class Square:
    def __init__(self, p1, p2, sides):
        self.p1, self.p2 = p1, p2
        self.sides = []
        self.setSides(sides)

    def setSides(self, sides):
        points = self.p1, np.array([self.p1[0], self.p2[1]]), self.p2, np.array([self.p2[0], self.p1[1]])
        for side in sides:
            quo = side["quo"]
            signs = [sign(quo(points[i][0], points[i][1])) for i in range(4)]
            if len(set(signs)) != 1:
                arrx = sorted([(self.p1[0], 1), (self.p2[0], 1), (side["p1"][0], 2), (side["p2"][0], 2)])
                arry = sorted([(self.p1[1], 1), (self.p2[1], 1), (side["p1"][1], 2), (side["p2"][1], 2)])
                if arrx[0][1] != arrx[1][1] and arry[0][1] != arry[1][1]:
                    self.sides += [side]

    def intersected(self, quo):
        points = self.p1, np.array([self.p1[0], self.p2[1]]), self.p2, np.array([self.p2[0], self.p1[1]])
        signs = [sign(quo(points[i][0], points[i][1])) for i in range(4)]
        if len(set(signs)) != 1:
            return True
        else: return False

class SquaredField:

    def __init__(self, p1, p2, sides):
        self.sides = sides
        self.amount = len(sides)
        self.depth = 0
        self.dia = len(sides)
        self.size = p2[0] - p1[0]
        self.p1 = p1
        self.p2 = p2

        self.tree = [[[Square(p1, p2, sides)]]]

    def addDepth(self):
        self.tree.append([])
        self.depth += 1

    def divideLayer(self, layer):
        assert self.depth == layer or self.depth == layer - 1, 'layer out of depth'
        if self.depth == layer - 1: self.addDepth()

        dia = 0
        for i in range(2**layer):
            self.tree[layer].append([])
            for j in range(2**layer):
                p1 = self.tree[0][0][0].p1[::]
                p2 = self.tree[0][0][0].p2[::]
                p2[0] = p1[0] + self.size * (i+1) / 2**layer
                p2[1] = p1[1] + self.size * (j+1) / 2**layer
                p1[0] += self.size * i / 2**layer
                p1[1] += self.size * j / 2**layer
                prevSides = self.tree[layer - 1][i // 2][j // 2].sides
                self.tree[layer][i] += [Square(p1, p2, prevSides)]
                if len(self.tree[layer][i][-1].sides) > dia:
                    dia = len(self.tree[layer][i][-1].sides)
        self.dia = dia

    def divideField(self):
        while 2**self.depth < self.amount and self.dia > 2:
            self.divideLayer(self.depth + 1)

    def sideIndsFromRadius(self, x0, y0, radius, depth = -1):
        circle = lambda x, y: (x - x0)**2 + (y - y0)**2 - radius**2
        x1 = int((x0 - self.p1[0]) * 2**depth // self.size)
        y1 = int((x1 - self.p1[1]) * 2**depth // self.size)
        stack = [(self.tree[depth][x1][y1], x1, y1)]
        sides = set()
        checked = []
        while stack:
            sqr, xi, yi = stack.pop()
            checked.append((xi, yi))
            for i in sqr.sides:
                sides.add(i["i"])
            for i in range(3):
                if xi - 1 + i < 0 or xi + i - 1 >= len(self.tree[depth]): continue
                for j in range(3):
                    if yi - 1 + j < 0 or yi - 1 + j >= len(self.tree[depth][xi - 1 + i]): continue
                    if self.tree[depth][i][j].intersected(circle) and (xi - 1 + i, yi - 1 + j) not in checked:
                        stack.append((self.tree[depth][xi - 1 + i][yi - 1 + j], xi - 1 + i, yi - 1 + j))
        return sides


    def checkPoint(self, point):
        depth = i = j = 0
        while len(self.tree[depth][i][j].sides) > 0 and depth < self.depth:
            depth += 1
            i = int((point[0] - self.p1[0]) * 2**depth // self.size)
            j = int((point[1] - self.p1[1]) * 2**depth // self.size)
        if len(self.tree[depth][i][j].sides) > 0:
            # calculate sides from all neighbours including (i, j) cell
            print("Failed")
        else:

            sideIndsOnCircle = set()
            radius = 0
            cellSize = self.size / 2**depth
            while len(sideIndsOnCircle) == 0:
                radius += cellSize
                print(radius, depth)
                sideIndsOnCircle = self.sideIndsFromRadius(point[0], point[1], radius, depth)
            print(sideIndsOnCircle)

            while len(sideIndsOnCircle) > self.dia + 2 and depth < self.depth:
                sideIndsOnCircle = set()
                depth += 1
                radius = 0
                cellSize = self.size / 2**depth
                while len(sideIndsOnCircle) == 0:
                    radius += cellSize
                    print(radius, depth)
                    sideIndsOnCircle = self.sideIndsFromRadius(point[0], point[1], radius, depth)
                print(sideIndsOnCircle)


        
        ...

def test(vertices, points):

    sides = []
    for i in range(len(vertices) - 1):
        nor = np.dot(np.array([0, -1, 1, 0]).reshape(2,2), vertices[i+1] - vertices[i])
        c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
        def lineQuo(x, y, a = nor[0], b = nor[1], c = c): # c = line(0, 0)
            return a * x + b * y + c
        sides.append({"quo": lineQuo, "nor": nor, "p1": vertices[i], "p2": vertices[i+1], "p0": vertices[i-1 if i != 0 else len(vertices) - 2], "p3": vertices[i+2 if i < len(vertices) - 2 else 1], "i":i})



    startSquare = calcStartSquare(np.concatenate([vertices, points]))
    field = SquaredField(startSquare[0], startSquare[1], sides)

    t0 = time.time()
    field.divideField()
    t1 = time.time()
    print(field.dia, t1 - t0)
    field.checkPoint(points[0])
    print(time.time() - t1)
    
    # res = []
    # for point in points:
    #     mindist, nPoint = calcNearest(sides, point)
    #     if mindist == 0:
    #         res += [[mindist, nPoint[0], nPoint[1]]]
    #     else:
    #         res += [[mindist * (-1)**(not isInPolygon(sides, point)), nPoint[0], nPoint[1]]]
    # return res

def isInPolygon(sides, point):
    timesCrosses = 0

    for side in sides:
        if side["nor"][0] == 0:
            if side["quo"](point[0], point[1]) == 0:
                if (side["p0"][1] > point[1]) != (side["p3"][1] > point[1]) and side["p3"][0] > point[0]:
                    timesCrosses += 1
        else:
            xi = -side["quo"](0, point[1]) / side["nor"][0]
            if side == sides[-1] and xi > point[0] and xi == side["p2"][0] and point[1] == side["p2"][1]:
                if (side["p1"][1] > point[1]) != (side["p3"][1] > point[1]) and side["p1"][1] != point[1] and side["p3"][1] != point[1]:
                    timesCrosses += 1
            elif xi > point[0] and xi == side["p1"][0] and point[1] == side["p1"][1]:
                if (side["p0"][1] > point[1]) != (side["p2"][1] > point[1]) and side["p0"][1] != point[1] and side["p2"][1] != point[1]:
                    timesCrosses += 1                                    # В случае совпадения проверяет: если предыдущая и следующая точки лежат по разные стороны от прямой, то добавить 1 иначе ничего
            elif xi > point[0] and (side["p2"][1] > point[1]) == (side["p0"][1] < point[1]) and side["p2"][1] != point[1] and side["p0"][1] != point[1]:
                timesCrosses += 1

    return not timesCrosses % 2 == 0


f = open(entries[1], 'r', encoding='utf8')

t = int(f.readline().strip('\n'))
verticesi, pointsi = [], []
for _ in range(t):
    vertices, points = readTest(f)
    verticesi += [vertices]
    pointsi += [points]
    
f.close()

for i in range(t):
    # print(verticesi[i], pointsi[i])
    answers = test(verticesi[i], pointsi[i])
    # for [dist, x, y] in answers:
        # print(round(dist, 8), round(x, 8), round(y, 8))
    ...