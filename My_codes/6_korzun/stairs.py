from sys import argv as entries
from time import time

start = time()

if len(entries) < 3: entries.append(True)

n = int(entries[1])

ways = {}
ways[1] = 1
ways[2] = 2
ways[3] = 4

def countWay(n):
    if n not in ways: # мемоизация словарём...
        for i in range(len(ways) + 1, n):
            ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
        ways[n] = countWay(n - 3) + countWay(n - 1) + countWay(n - 2)
    return ways[n]
ans = countWay(n)
print(time() - start, end = ' ')
if entries[2] != 'False': print(ans)