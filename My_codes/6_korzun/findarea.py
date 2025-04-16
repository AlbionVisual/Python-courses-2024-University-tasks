from sys import argv as entries
from collections import deque

with open(entries[1], 'r', encoding='utf8') as f:

    table = []
    for line in f:
        table += [line.strip('\n')]
    
    height = len(table)
    width = len(table[0])
    if table[height//2][width//2] != '*':
        # err = 'not in center'
        print('Error')
    else:
        graph = {}
        amount = 0
        for i in range(height):
            for j in range(width):
                if table[i][j] == '*':
                    amount += 1
                    graph[(i, j)] = []
                    if i > 0 and table[i-1][j] == '*': graph[(i, j)] += [(i-1,j)]
                    if j > 0 and table[i][j-1] == '*': graph[(i, j)] += [(i,j-1)]
                    if i < height - 1 and table[i+1][j] == '*': graph[(i, j)] += [(i+1,j)]
                    if j < width - 1 and table[i][j+1] == '*': graph[(i, j)] += [(i,j+1)]
        
        searched = [(height // 2, width // 2)]
        Q = deque([(height // 2, width // 2)])
        while Q:
            el0 = Q.popleft()
            for eli in graph[el0]:
                if eli not in searched:
                    searched += [eli]
                    Q.append(eli)
        
        # print(amount)
        # print(len(searched))
        print(amount if amount == len(searched) else 'Error')