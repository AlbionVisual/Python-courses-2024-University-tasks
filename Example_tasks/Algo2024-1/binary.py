import sys

n = int(sys.argv[1])
i = 0
while (2**(i+1) <= n):
    i = i + 1

s = ''
while (i >= 0):
    if (n - 2**i >= 0):
        n = n - 2**i
        s = s + '1'
    else:
        s = s + '0'
    i = i - 1

print(s)