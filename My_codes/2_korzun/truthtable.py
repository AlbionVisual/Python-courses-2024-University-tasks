import sys

n = int(sys.argv[1])

res = []

for i in range(2**n):
    num = i
    j = 0
    res.append([])
    for j in range(n):
        res[i].insert(0,num % 2)
        num //= 2


for i in reversed(res):
    print(i)