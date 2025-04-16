from sys import argv as entries
from collections import deque
from time import time

class LRUCash:

    def __init__(self, size):
        self.n = size
        self.visited = {}
        self.queue = deque([])
    
    def add(self, x):
        if x not in self.visited:
            self.visited[x] = 1
        else:
            self.visited[x] += 1
            if x in self.queue: self.queue.remove(x)
        self.queue.append(x)
        if len(self.queue) > self.n:
            to_del = self.queue.popleft()
            del self.visited[to_del]
    
    def print(self):
        for el in reversed(self.queue):
            print(el, self.visited[el])

with open(entries[1], 'r', encoding='utf8') as f:
    # start = time()
    lru = LRUCash(int(entries[2]))
    for line in f:
        lru.add(line.strip('\n'))
    
    lru.print()
    # print('\n', time() - start)