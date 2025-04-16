from sys import argv as entries
from collections import defaultdict
from time import time

start = time()

graph = defaultdict(list)
with open(entries[1], 'r', encoding='utf8') as f:
    for line in f:
        v1, v2, weight = line.strip().split('\t')
        graph[v1].append((v2, int(weight)))
        graph[v2].append((v1, int(weight)))

searched = set([list(graph.keys())[0]])
total_weight = 0
edges = []

while len(searched) < len(graph):
    min_weight = float('inf')
    min_edge = None
    for v in searched:
        for node, weight in graph[v]:
            if node not in searched and weight < min_weight:
                min_weight = weight
                min_edge = (v, node, weight)
    if min_edge:
        u, v, weight = min_edge
        searched.add(v)
        total_weight += weight
        edges.append(min_edge)

print(time() - start, total_weight, edges)