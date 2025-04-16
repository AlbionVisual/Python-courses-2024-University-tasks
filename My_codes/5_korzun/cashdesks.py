from simplequeue import Queue
from sys import argv as entries
from random import choices

def findMin(queues):
    ind = 0; min = len(queues[0])
    for i in range(len(queues)):
        if len(queues[i]) < min:
            min, ind = len(queues[i]), i
    return ind
            

# entries = ["cashdesks.py", 3, 8, 20]
[N, C, T] = [int(i) for i in entries[1:4]]

desks = [Queue() for _ in range(C)]
res = []

for _ in range(T):

    people = choices([1,2,3,4,5], weights=[0.45,0.25,0.15,0.10, 0.05], k=N)
    for men in people:
        where = findMin(desks)
        desks[where].enqueue(men)
    
    res += [sum([sum(list(desk.items)) for desk in desks]) / C]

    for desk in desks:
        men = desk.dequeue()
        if type(men) != str and men > 1: desk.appendleft(men - 1)
        
print(res)