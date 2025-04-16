from sys import argv as entries
from collections import deque

with open(entries[1], 'r', encoding='utf8') as f:

    films = {}
    for line in f:
        a, b = line.strip('\n').split('\t')
        if b in films: films[b] += [a]
        else: films[b] = [a]

    graph = {}
    for film in films:
        for actor1 in films[film]:
            for actor2 in films[film]:
                if actor2 != actor1:
                    if actor1 in graph:
                        graph[actor1] += [actor2]
                    else: graph[actor1] = [actor2]

    dists = {}
    dists[entries[2]] = 0
    Q = deque([entries[2]])
    while Q:
        el0 = Q.popleft()
        for eli in graph[el0]:
            if eli not in dists:
                dists[eli] = dists[el0] + 1
                Q.append(eli)
    
    print(dists[entries[3]] if entries[3] in dists else None)