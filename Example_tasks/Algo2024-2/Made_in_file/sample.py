import sys, random

if len(sys.argv) == 1:
    n = 1
    k = n
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
    k = n
else:
    n = int(sys.argv[1])
    k = int(sys.argv[2])

lst = list(range(n))

for i in range(n):
    r = random.randrange(i, n)
    tmp = lst[r]
    lst[r] = lst[i]
    lst[i] = tmp

print([lst.pop() for i in range(k)])            # before: lst[-k:]