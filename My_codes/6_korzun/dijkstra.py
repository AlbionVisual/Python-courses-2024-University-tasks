from sys import argv as entries
from collections import deque
# from pprint import pp as print

with open(entries[1], 'r', encoding='utf8') as f:
    graph = {}
    for line in f:
        a, b, w = line.strip('\n').split('\t')
        if a in graph: graph[a] += [{b:w}]
        else: graph[a] = [{b:w}]
        if b in graph: graph[b] += [{a:w}]
        else: graph[b] = [{a:w}]
    for el in graph:
        graph[el].sort(key=lambda x: int(list(x.values())[0]))
    # print(graph, sort_dicts=False)

    city = entries[2]
    dists = {city: 0}
    S = deque([city])
    while S:
        node = S.pop()
        searched = [node]
        for el in graph[node]:
            for i in el:
                key = i
                val = int(el[key])
            if key not in searched:
                if key not in dists:
                    dists[key] = dists[node] + val
                    S.appendleft(key)
                else:
                    if dists[key] > dists[node] + val:
                        dists[key] = dists[node] + val
    
    ans = []
    for el in dists:
        ans += [(el, dists[el])]
    ans.sort(key=lambda x: x[1])
    print('Top 5 nearest cities:')
    for i in ans[1:6]:
        print(i)
    print('Top 5 distant cities:')
    for i in ans[-5:]:
        print(i)