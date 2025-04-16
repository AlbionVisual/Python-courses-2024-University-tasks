from sys import argv as entries
from random import randrange as rand
from time import time

def merge_sort(arr, left, right):

    def merge(arr, left, right, mid):
        mid += 1
        right += 1
        arr1, arr2 = arr[left:mid], arr[mid:right]
        newarr = []
        if len(arr1) > len(arr2): arr1, arr2 = arr2, arr1
        id1 = id2 = 0
        while id1 + id2 < len(arr1) + len(arr2):
            if id2 >= len(arr2) or (id1 < len(arr1) and arr1[id1] < arr2[id2]): 
                newarr.append(arr1[id1])
                id1 += 1
            else: 
                newarr.append(arr2[id2])
                id2 += 1
        arr[left:right] = newarr
        return arr
    
    if (left < right):
        mid = left + (right - left) // 2
        arr = merge_sort(arr, left, mid)        # arr =  -useless
        arr = merge_sort(arr, mid + 1, right)
        arr = merge(arr, left, right, mid)
        return arr
    return arr

n, m, k = [int(i) for i in entries[1:]]
arr = [rand(1, m) for _ in range(n)]

start = time()
arr = merge_sort(arr, 0, len(arr))
end = time()

if k > 0: print(end - start, arr[-k:])
else: print(end - start)