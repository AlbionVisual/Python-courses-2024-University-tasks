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
                        graph[actor1] += [(actor2, film)]
                    else: graph[actor1] = [(actor2, film)]

    dists = {}
    dists[entries[2]] = (0, [])
    Q = deque([entries[2]])
    while Q:
        el0 = Q.popleft()
        for eli in graph[el0]:
            if eli[0] not in dists:
                dists[eli[0]] = (dists[el0][0] + 1, dists[el0][1] + [(el0, eli[1], eli[0])])
                Q.append(eli[0])
    
    if entries[3] in dists:
        print('Distance: ', dists[entries[3]][0])
        for start, film, end in dists[entries[3]][1]:
            braces = ("{'", "'}")
            print(f'{start} was with {end} in {braces[0] + film + braces[1]}')
        # Kevin Bacon was with Tom Hanks in {'Apollo 13'}
    else: print(None)