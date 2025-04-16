import sys

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1

count = 1
max = -1

while n != 1:
    if max < n:
        max = n
    count += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1


print([count, max])