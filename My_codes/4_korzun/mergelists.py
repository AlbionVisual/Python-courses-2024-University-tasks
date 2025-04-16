from random import randrange as rand
from sys import argv as entries

def merge_list(arr1, arr2):
    arr = []
    if len(arr1) > len(arr2): arr1, arr2 = arr2, arr1
    id1 = id2 = 0
    while id1 + id2 < len(arr1) + len(arr2):
        if id2 >= len(arr2) or (id1 < len(arr1) and arr1[id1] < arr2[id2]): 
            arr.append(arr1[id1])
            id1 += 1
        else: 
            arr.append(arr2[id2])
            id2 += 1

    return arr

n = int(entries[1])
a = sorted([rand(0, n + 1) for _ in range(rand(1, n + 1))])
b = sorted([rand(0, n + 1) for _ in range(rand(1, n + 1))])

print(a, b, merge_list(a, b), sep='\n')