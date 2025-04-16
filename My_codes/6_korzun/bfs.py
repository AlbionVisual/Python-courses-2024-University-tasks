from sys import argv as entries
from collections import deque

with open(entries[1], 'r', encoding='utf8') as f:
    graph = {}
    for line in f:
        a, b = line.strip('\n').split('\t')
        if a in graph: graph[a] += [b]
        else: graph[a] = [b]
        if b in graph: graph[b] += [a]
        else: graph[b] = [a]
    
    searched = {entries[2],}
    Q = deque([entries[2]])
    while Q:
        el0 = Q.popleft()
        for eli in graph[el0]:
            if eli not in searched:
                searched.add(eli)
                Q.append(eli)
    
    print(searched)