from minheap import MinHeap
from sys import argv as entries
from random import randrange
from time import time

start = time()

n, m, k = [int(i) for i in entries[1:]]
heap = MinHeap([randrange(1, m) for _ in range(n)])

print(time() - start, heap.sort()[-k:] if k != 0 else '')