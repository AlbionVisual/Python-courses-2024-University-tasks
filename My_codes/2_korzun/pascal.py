import sys

n = int(sys.argv[1]) + 1

pasc = [[0] * i for i in range(1, n + 1)]
pasc[0][0] = 1
for i in range(1, n):
    for j in range(i + 1):
        if j == 0 or j == i:
            pasc[i][j] = 1
        else:
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]

print(pasc)