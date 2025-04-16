import sys

n, m = int(sys.argv[1]), int(sys.argv[2])

res = m + 1
if m >= n:
    res = 2 * n - m - 1

print(res)