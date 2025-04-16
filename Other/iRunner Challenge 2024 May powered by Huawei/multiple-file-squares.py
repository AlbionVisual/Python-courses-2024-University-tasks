import numpy as np
from sys import argv as entries

# entries = [0, "./iRunner Challenge 2024 May powered by Huawei/one-figure-test.txt"]

def sign(c):
    return 1 if c > 0 else -1 if c < 0 else 0

def sqrlen(vec):
    return vec[0]**2 + vec[1]**2

veclens = {} # memoising
def veclen(vec):
    # global veclens
    # if (np.abs(vec[0]), np.abs(vec[1])) not in veclens: 
    #     veclens[(np.abs(vec[0]), np.abs(vec[1]))] = np.sqrt(vec[0]**2 + vec[1]**2)
    # return veclens[(np.abs(vec[0]), np.abs(vec[1]))]
    return (vec[0]**2 + vec[1]**2)**.5

def min(obj):
    ind = 0
    for i in range(1, len(obj)):
        if obj[i] < obj[ind]: ind = i
    return obj[ind], ind

def calcDistance(side, point):
    return abs(side['c'] + side['nor'][0] * point[0] + side['nor'][1] * point[1]) / veclens[tuple(side["nor"])]

def distPoint(side, point, dist):
    xi = point[0] - sign(side['c'] + side['nor'][0] * point[0] + side['nor'][1] * point[1]) * dist * side["nor"][0] / veclens[tuple(side["nor"])]
    yi = point[1] - sign(side['c'] + side['nor'][0] * point[0] + side['nor'][1] * point[1]) * dist * side["nor"][1] / veclens[tuple(side["nor"])]
    return np.array([xi, yi])

def readTest(f = -1):
    # n = int(f.readline().strip('\n'))
    # s = f.readline().strip('\n')
    # vertices = np.array([float(i) for i in s.split()]).reshape(n, 2)
    # N = int(f.readline().strip('\n'))
    # points = []
    # for _ in range(N):
    #     s = f.readline().strip('\n')
    #     points.append([float(i) for i in s.split()])
    # points = np.array(points)
    # vertices = np.append(vertices, np.array([vertices[0]]), axis=0)
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
    def __init__(self, p1, p2, sides = []):
        self.p1, self.p2 = p1, p2
        self.size = self.p2[0] - self.p1[0]
        self.sides = []
        if sides != []:
            self.setSides(sides)

    def setSides(self, sides):
        # points = self.p1, np.array([self.p1[0], self.p2[1]]), self.p2, np.array([self.p2[0], self.p1[1]])
        for side in sides:
            # quo = side["quo"]
            # # signs = [sign(quo(points[i][0], points[i][1])) for i in range(4)]
            # side['c'] + side['nor'][0] * x + side['nor'][1] * y
            sign1 = sign(side['c'] + side['nor'][0] * self.p1[0] + side['nor'][1] * self.p1[1])
            sign2 = sign(side['c'] + side['nor'][0] * self.p1[0] + side['nor'][1] * self.p2[1])
            sign3 = sign(side['c'] + side['nor'][0] * self.p2[0] + side['nor'][1] * self.p2[1])
            sign4 = sign(side['c'] + side['nor'][0] * self.p2[0] + side['nor'][1] * self.p1[1])
            # if len(set(signs)) != 1:
            if sign1 != sign2 or sign1 != sign4 or sign3 != sign4 or sign2 != sign3:
                arrx = sorted([(self.p1[0], 1), (self.p2[0], 1), (side["p1"][0], 2), (side["p2"][0], 2)])
                arry = sorted([(self.p1[1], 1), (self.p2[1], 1), (side["p1"][1], 2), (side["p2"][1], 2)])
                if arrx[0][1] != arrx[1][1] and arry[0][1] != arry[1][1]:
                    self.sides += [side]
        # for side in sides:
        #     if self.intersected(side['quo']):
        #         self.sides += [side]

    def intersected(self, quo):
        # points = self.p1, np.array([self.p1[0], self.p2[1]]), self.p2, np.array([self.p2[0], self.p1[1]])
        # signs = [sign(quo(points[i][0], points[i][1])) for i in range(4)]
        sign1 = sign(quo(self.p1[0], self.p1[1]))       # 2e-6
        sign2 = sign(quo(self.p1[0], self.p2[1]))
        sign3 = sign(quo(self.p2[0], self.p2[1]))
        sign4 = sign(quo(self.p2[0], self.p1[1]))
        # ans = [0, 0, 0, 0] # up, right, down, left
        # if sign1 != sign2:
        #     ans[3] = 1
        # if sign1 != sign4:
        #     ans[2] = 1
        # if sign3 != sign2:
        #     ans[0] = 1
        # if sign3 != sign4:
        #     ans[1] = 1
        # return ans
        return sign1 == sign2 and sign3 == sign4 and sign2 == sign3
        # if len(set(signs)) != 1:
        #     return True
        # else: return False

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

    def addLayer(self):
        self.tree.append([])
        self.depth += 1
        dia = 0
        for i in range(2**self.depth):
            self.tree[self.depth].append([])
            for j in range(2**self.depth):
                p1 = self.tree[self.depth - 1][i//2][j//2].p1[::]
                p2 = self.tree[self.depth - 1][i//2][j//2].p2[::]
                size = self.tree[self.depth - 1][i//2][j//2].size / 2
                p1[0] += (i % 2) * size
                p1[1] += (j % 2) * size
                p2[0] -= (i % 2 == 0) * size
                p2[1] -= (j % 2 == 0) * size
                self.tree[self.depth][i].append(Square(p1, p2, self.tree[self.depth - 1][i//2][j//2].sides))
                if dia < len(self.tree[self.depth][i][j].sides): dia = len(self.tree[self.depth][i][j].sides)
        self.dia = dia

    def divideField(self):
        while 2**self.depth < self.amount and self.dia > (2 if self.amount < 20 else self.amount / 10):
            self.addLayer()

    def getCells(self, radius, x0 = 0, y0 = 0, depth = 6):
        preva = 1 # cos or with x
        prevb = 0 # sin or for y
        size = self.size
        p1 = self.p1
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
                    if b > 1: b = 1
                    a = (1 - b**2)**.5
                else:
                    b = prevb - cellsize / radius
                    if b < -1: b = -1
                    a = -(1 - b**2)**.5
                    phase = 2
            else:
                if prevb > 0:
                    a = preva - cellsize / radius
                    if a < -1: a = -1
                    b = (1 - a**2)**.5
                    phase = 1
                else:
                    a = cellsize / radius + preva
                    if a > 1: a = 1
                    b = -(1 - a**2)**.5
                    phase = 3
                
            preva = a
            prevb = b
            point = (x0 + a*radius, y0 + b*radius)
            cell = (int((point[0] - p1[0]) * 2**depth // size), int((point[1] - p1[1]) * 2**depth // size))
            if cell[0] >= 0 and cell[1] >= 0 and cell[0] < 2**depth and cell[1] < 2**depth: cells += [cell]    
        return cells

    def sideIndsFromRadius(self, x0, y0, radius, depth = -1):
        s = set()
        # if radius <= self.size / 2**depth:
        #     cells = [(int((x0 - self.p1[0]) * 2**depth // self.size), int((y0 - self.p1[1]) * 2**depth // self.size))]
        #     if cells[0][0] - 1 >= 0: cells += [(cells[0][0] - 1, cells[0][1])]
        #     if cells[0][1] - 1 >= 0: cells += [(cells[0][0], cells[0][1] - 1)]
        #     if cells[0][0] + 1 < 2**depth: cells += [(cells[0][0] + 1, cells[0][1])]
        #     if cells[0][1] + 1 < 2**depth: cells += [(cells[0][0], cells[0][1] + 1)]
        #     for cell in cells:
        #         for side in self.tree[depth][cell[0]][cell[1]].sides:
        #             s.add(side["i"])
        if radius <= 2 * self.size / 2**depth:
            cell = (int((x0 - self.p1[0]) * 2**depth // self.size), int((y0 - self.p1[1]) * 2**depth // self.size))
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if cell[0] + i >= 0 and cell[0] + i < 2**depth and cell[1] + j >= 0 and cell[1] + j < 2**depth:
                        for side in self.tree[depth][cell[0] + i][cell[1] + j].sides:
                            s.add(side['i'])
        elif radius <= 3 * self.size / 2**depth:
            cell = (int((x0 - self.p1[0]) * 2**depth // self.size), int((y0 - self.p1[1]) * 2**depth // self.size))
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if cell[0] + i >= 0 and cell[0] + i < 2**depth and cell[1] + j >= 0 and cell[1] + j < 2**depth:
                        for side in self.tree[depth][cell[0] + i][cell[1] + j].sides:
                            s.add(side['i'])
        else:
            for x, y in self.getCells(radius, x0, y0, depth if depth != -1 else self.depth):
                for side in self.tree[depth][x][y].sides:
                    s.add(side["i"])
        return s

    def checkPoint(self, point):
        depth = i = j = 0
        while len(self.tree[depth][i][j].sides) > 0 and depth < self.depth:
            depth += 1
            i = int((point[0] - self.p1[0]) * 2**depth // self.size)
            j = int((point[1] - self.p1[1]) * 2**depth // self.size)
        if len(self.tree[depth][i][j].sides) > 0:
            sideIndsOnCircle = self.sideIndsFromRadius(point[0], point[1], self.size / 2**depth, depth)
            for side in self.tree[depth][i][j].sides:
                sideIndsOnCircle.add(side['i'])
        else:
            sideIndsOnCircle = set()
            cellSize = self.size / 2**depth
            dists = [(point[0] - self.p1[0]) % cellSize,
                    (point[1] - self.p1[1]) % cellSize,
                    cellSize - (point[1] - self.p1[1]) % cellSize,
                    cellSize - (point[0] - self.p1[0]) % cellSize]
            radius = min(dists)[0]
            while len(sideIndsOnCircle) == 0:
                radius += cellSize / 2
                # print('1', radius, depth)
                sideIndsOnCircle = self.sideIndsFromRadius(point[0], point[1], radius, depth)
            # print('1', sideIndsOnCircle)
            for i in self.sideIndsFromRadius(point[0], point[1], radius + max(dists), (depth + 1 if depth < self.depth else depth)):
                sideIndsOnCircle.add(i)
            radius -= cellSize / 2 - min(dists)[0]

            while len(sideIndsOnCircle) > self.dia + 1 and depth < self.depth:
                sideIndsOnCircle = set()
                depth += 1
                cellSize = self.size / 2**depth
                while len(sideIndsOnCircle) == 0:
                    radius += cellSize / 2
                    # print('2', radius, depth)
                    sideIndsOnCircle = self.sideIndsFromRadius(point[0], point[1], radius, depth)
                # print('2', sideIndsOnCircle)
                for i in self.sideIndsFromRadius(point[0], point[1], radius, depth + 1 if depth < self.depth else depth):
                    sideIndsOnCircle.add(i)
                radius -= cellSize / 2

        mindist = 1e10
        M = 0

        for i in sideIndsOnCircle:
            side = self.sides[i]
            dist = calcDistance(side, point)
            M = distPoint(side, point, dist)
            if ((side["p1"] <= M)[0] != (M <= side["p2"])[0] or (side["p1"] <= M)[1] != (M <= side["p2"])[1]):
                if sqrlen(side["p1"] - point) > sqrlen(side["p2"] - point):  
                    dist, M = veclen(side["p2"] - point), side["p2"]
                else: 
                    dist, M = veclen(side["p1"] - point), side["p1"]
            if dist < mindist:
                mindist = dist
                nPoint = M

        return mindist**2, nPoint

    def sidesRightToThePoint(self, point):
        
        x = int((point[0] - self.p1[0]) * 2**self.depth // self.size)
        y = int((point[1] - self.p1[1]) * 2**self.depth // self.size)

        s = set()

        while x < 2**self.depth:
            for side in self.tree[self.depth][x][y].sides:
                s.add(side['i'])
            x += 1
        
        return s



def test(vertices, points):
    global veclens
    veclens = {}
    sides = []
    for i in range(len(vertices) - 1):
        nor = np.dot(np.array([0, -1, 1, 0]).reshape(2,2), vertices[i+1] - vertices[i])
        c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
        # def lineQuo(x, y, a = nor[0], b = nor[1], c = c): # c = line(0, 0)
        #     return a * x + b * y + c
        sides.append({"c": c, "nor": nor, "p1": vertices[i], "p2": vertices[i+1], "p0": vertices[i-1 if i != 0 else len(vertices) - 2], "p3": vertices[i+2 if i < len(vertices) - 2 else 1], "i":i})
        veclens[tuple(sides[-1]['nor'])] = veclen(nor)


    startSquare = calcStartSquare(np.concatenate([vertices, points]))
    field = SquaredField(startSquare[0], startSquare[1], sides)
    field.divideField()
    
    res = []
    for point in points:
        mindist, nPoint = field.checkPoint(point)
        sideIndecesToTest = field.sidesRightToThePoint(point)
        sidesToTest = []
        for i in sideIndecesToTest: sidesToTest.append(sides[i])
        if mindist == 0:
            res += [[mindist, nPoint[0], nPoint[1]]]
        else:
            res += [[mindist * (-1)**(not isInPolygon(sidesToTest, point)), nPoint[0], nPoint[1]]]
    return res

def isInPolygon(sides, point):
    timesCrosses = 0

    for side in sides:
        if side["nor"][0] == 0:
            if side["c"] + point[0] * side['nor'][0] + point[1] * side['nor'][1] == 0:
                if (side["p0"][1] > point[1]) != (side["p3"][1] > point[1]) and side["p3"][0] > point[0]:
                    timesCrosses += 1
        else:
            xi = ( - side['c'] - side['nor'][1] * point[1]) / side["nor"][0]
            if side['i'] == len(sides) - 1 and xi > point[0] and xi == side["p2"][0] and point[1] == side["p2"][1]:
                if (side["p1"][1] > point[1]) != (side["p3"][1] > point[1]) and side["p1"][1] != point[1] and side["p3"][1] != point[1]:
                    timesCrosses += 1
            elif xi > point[0] and xi == side["p1"][0] and point[1] == side["p1"][1]:
                if (side["p0"][1] > point[1]) != (side["p2"][1] > point[1]) and side["p0"][1] != point[1] and side["p2"][1] != point[1]:
                    timesCrosses += 1                                    # В случае совпадения проверяет: если предыдущая и следующая точки лежат по разные стороны от прямой, то добавить 1 иначе ничего
            elif xi > point[0] and (side["p2"][1] > point[1]) == (side["p1"][1] < point[1]) and side["p2"][1] != point[1] and side["p1"][1] != point[1]:
                timesCrosses += 1

    return not timesCrosses % 2 == 0


# f = open(entries[1], 'r', encoding='utf8')

# t = int(f.readline().strip('\n'))
t = int(input())
verticesi, pointsi = [], []
for _ in range(t):
    vertices, points = readTest()
    verticesi += [vertices]
    pointsi += [points]
    
# f.close()

# f = open("output.txt", 'w', encoding='utf8')

for i in range(t):
    answers = test(verticesi[i], pointsi[i])
    for [dist, x, y] in answers:
        print(dist, x, y)
        # f.write(str(round(dist, 8)) + ' ' + str(round(x, 8)) + ' ' + str(round(y, 8)) + '\n')

# f.close()