from sys import argv as entries

with open(entries[1], 'r', encoding='utf8') as f:
    graph = {}
    for line in f:
        a, b = line.strip('\n').split('\t')
        if a in graph: graph[a] += [b]
        else: graph[a] = [b]
        if b in graph: graph[b] += [a]
        else: graph[b] = [a]
    
    searched = set()
    S = [entries[2]]
    while S:
        el_0 = S.pop()
        if el_0 not in searched:
            searched.add(el_0)
            for el_i in graph[el_0]:
                S.append(el_i)
    
    print(searched)