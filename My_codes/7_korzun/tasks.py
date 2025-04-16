from sys import argv as entries
# from pprint import pp as print
from time import time


s = entries[1]
tasks = [tuple([int(j) for j in i.split(',')]) for i in s.strip().split()]


start = time()
tasks.sort(key=lambda x: x[1])
ans = tasks[:1]
for i in tasks[1:]:
    if ans[-1][1] <= i[0]:
        ans.append(i)
print(time() - start, len(ans), ans)