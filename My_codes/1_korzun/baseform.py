import sys, math

# show your number in a different baseform (< 10)

n, base = int(sys.argv[1]), int(sys.argv[2])

i = 0
while (base**(i+1) <= n):
    i += 1

s = 0
while (i >= 0):
    if (n - base**i >= 0):
        s += math.floor(n / base**i)*(10**i)
        n = n % (base**i)
    i = i - 1

print(s)