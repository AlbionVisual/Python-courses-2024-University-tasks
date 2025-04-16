import sys

def findMaxMin(matr):
    min = max = matr[0][0]

    for i in matr:
        for j in i:
            if j > max:
                max = j
            if j < min:
                min = j
    return min, max

matr = [j.split() for j in [i.strip(' ') for i in sys.argv[1].split(',')]]
matr = [[int(j) for j in i] for i in matr]

min, max = findMaxMin(matr)

if max == min:
    if max != 0:
        matr = [[1] * len(i) for i in matr]
else:

    delta = max - min
    matr = [[(j - min) / delta for j in i] for i in matr]


print(matr)