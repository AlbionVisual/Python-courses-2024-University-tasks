import sys

# facto n, e. g. 36 = 2 * 2 * 3 * 3

n = int(sys.argv[1])

factor = 2
s = ''

while (n > 1):
    while (n % factor == 0):
        s += str(factor) + ' '
        n //= factor
    factor += 1

print(s)