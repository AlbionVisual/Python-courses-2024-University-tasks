import sys, math, time

start = time.time()

number = int(sys.argv[1])

n = int(math.log2(number))

s = int(1 / 2**(1/2) * 1000) / 1000.0

matr = [[s,s],[s,-s]]

z = [[0 for j in range(number)] for k in range(number)]

for i in range(1, n):
    size = 2**i
    next = z[:]

    for j in range(size):
        for k in range(size):
            next[j][2 * k] = next[j][2 * k + 1] = matr[j][k] * s
            if j >= size // 2:
                next[j + size // 2][k] = next[j + size][k + size] = matr[j][k]            

    matr = next


print(time.time() - start)

# rounding up elements in matrix
matr = [[int(j * 1000 + (0.5 if j >= 0 else - 0.5))/1000.0 for j in i] for i in matr]           # you didn't see that

print(time.time() - start)

# print(matr)