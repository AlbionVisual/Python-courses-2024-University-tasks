import sys, math

size = int(sys.argv[1])
n = int(math.log(size, 2))

h = [[0] * size for i in range(size)]
h[0][0] = 1

for k in range(n):
    for i in range(2**k):
        for j in range(2**k):
            h[i][j+2**k] = h[i][j]
            h[i+2**k][j] = h[i][j]
            h[i+2**k][j+2**k] = - h[i][j]

for i in range(size):
    s = ''
    for j in range(size):
        s += str(h[i][j]) + '\t'
    print(s)