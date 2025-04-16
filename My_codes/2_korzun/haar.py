import sys, math, time

# start = time.time()

size = int(sys.argv[1])

n = int(math.log2(size))

s = 1 / 2**(1/2)

matr = [[0 for j in range(size)] for k in range(size)]

for i in range(size):
    matr[0][i] = s**n

stroke = 1
ind = 0

while n > 0:

    for i in range(size):
        if ind >= 2**n:
            stroke += 1
            ind = 0
        matr[stroke][i] = s**n if ind < 2**(n-1) else -s**n
        matr[stroke][i] = int(matr[stroke][i] * 1000) / 1000.0
        ind += 1

    n -= 1

# print(time.time() - start)

print(matr)