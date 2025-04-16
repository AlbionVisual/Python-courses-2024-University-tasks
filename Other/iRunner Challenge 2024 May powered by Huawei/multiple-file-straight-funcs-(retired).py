import numpy as np
from sys import argv as entries

# entries = [0, "iRunner Challenge 2024 May powered by Huawei/final-test.txt"]

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

def distPoint(side, point, dist):
    xi = point[0] - sign(side["quo"](point[0], point[1])) * dist * side["nor"][0] / veclen(side["nor"])
    yi = point[1] - sign(side["quo"](point[0], point[1])) * dist * side["nor"][1] / veclen(side["nor"])
    return np.array([xi, yi])

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

def calcNearest(sides, point):
    distances = []
    nearestPoints = []

    for side in sides:
        dist = calcDistance(side, point)
        distances.append(dist)
        nearestPoints.append(distPoint(side, point, dist))

    mindist, ind = min(distances)
    M = nearestPoints[ind]

    if ((sides[ind]["p1"] <= M)[0] == (M <= sides[ind]["p2"])[0] and (sides[ind]["p1"] <= M)[1] == (M <= sides[ind]["p2"])[1]):
        return mindist**2, M
    elif sqrlen(sides[ind]["p1"] - point) > sqrlen(sides[ind]["p2"] - point):  
        return sqrlen(sides[ind]["p2"] - point), sides[ind]["p2"]
    else: 
        return sqrlen(sides[ind]["p1"] - point), sides[ind]["p1"]

def test(vertices, points):

    sides = []
    for i in range(len(vertices) - 1):
        nor = np.dot(np.array([0, -1, 1, 0]).reshape(2,2), vertices[i+1] - vertices[i])
        c = - nor[0] * vertices[i][0] - nor[1] * vertices[i][1]
        def lineQuo(x, y, a = nor[0], b = nor[1], c = c): # c = line(0, 0)
            return a * x + b * y + c
        sides.append({"quo": lineQuo, "nor": nor, "p1": vertices[i], "p2": vertices[i+1], "p0": vertices[i-1 if i != 0 else len(vertices) - 2], "p3": vertices[i+2 if i < len(vertices) - 2 else 1]})

    res = []
    for point in points:
        mindist, nPoint = calcNearest(sides, point)
        if mindist == 0:
            res += [[mindist, nPoint[0], nPoint[1]]]
        else:
            res += [[mindist * (-1)**(not isInPolygon(sides, point)), nPoint[0], nPoint[1]]]
    return res

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
                    timesCrosses += 1
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

f = open('answers.txt', 'w', encoding='utf8')
for i in range(t):
    answers = test(verticesi[i], pointsi[i])
    for [dist, x, y] in answers:
        # f.write(str(round(dist, 8)) + ' ' + str(round(x, 8)) + ' ' + str(round(y, 8)) + '\n')
        print(round(dist, 8), round(x, 8), round(y, 8))

f.close()
print("!!!  False answers  !!!")