from sys import argv as entries
from pprint import pp as print

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

    dists = {entries[2]: 0}
    newdists = dists.copy()
    err = ''
    for i in range(len(graph) - 1):
        for el in dists:
            for child in graph[el]:
                for k in child:
                    key = k
                    val = int(child[k])
                if key not in newdists:
                    newdists[key] = newdists[el] + val
                else:
                    if newdists[key] > newdists[el] + val:
                        if i == len(graph) - 1: err = 'negative cycle'
                        newdists[key] = newdists[el] + val
        dists = newdists.copy()

    if err: print(err)
    else: 
        ans = [(key, dists[key]) for key in dists]
        ans.sort(key=lambda x: x[1])
        print('Top 5 nearest cities:')
        for i in ans[1:6]: print(i)
        print('Top 5 distant cities:')
        for i in ans[-5:]: print(i)
