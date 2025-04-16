from sys import argv as entries

def toposort(graph):

    searched = set()
    stack = []
    
    def dfs(vert):
        searched.add(vert)
        
        for child in graph[vert]:
            if child not in searched:
                dfs(child)
        
        stack.append(vert)
    
    for vert in graph:
        if vert not in searched:
            dfs(vert)
    
    return stack

with open(entries[1], 'r', encoding='utf8') as f:
    graph = {}
    elems = set()
    for line in f:
        a, b = line.strip('\n').split('\t')
        elems.add(a)
        elems.add(b)
        if a in graph: graph[a] += [b]
        else: graph[a] = [b]
    for el in elems:
        if el not in graph:
            graph[el] = []
    
    print(toposort(graph))