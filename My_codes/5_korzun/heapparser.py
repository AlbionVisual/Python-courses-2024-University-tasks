from minheap import MinHeap
from sys import argv as entries

heap = MinHeap()

with open(entries[1], 'r', encoding='utf8') as f:

    ops = 0

    for line in f:
        line = line.strip('\n').split()
        if line[0] == 'push':
            heap.push(int(line[1]))
        elif line[0] == 'pop':
            if heap.pop() == 'heap is empty': break
        elif line[0] == 'update':
            heap.update(int(line[1]), int(line[2]))
        
        ops += 1



    print(ops, heap.get_data()[:10] if len(heap) != 0 else 'heap is empty')