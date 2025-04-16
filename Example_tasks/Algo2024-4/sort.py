from random import randrange as rand

def merge_sort(arr):
    def recursion(arr, left, right):

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
            recursion(arr, left, mid)
            recursion(arr, mid + 1, right)
            merge(arr, left, right, mid)
            return arr
        return arr

    recursion(arr, 0, len(arr))

def bubble_sort(arr):
    for i in range(len(arr)):
        isSorted = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSorted = False
        if isSorted: break

def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        id = i
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                id = j
        arr[i], arr[id] = arr[id], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        id = i
        while id >= 1 and arr[id] < arr[id - 1]:
            arr[id], arr[id - 1] = arr[id - 1], arr[id]
            id -= 1

def quick_sort(numbers):
    def partition(arr,low,high):
        s=arr[rand(low, high)]
        i=low
        j=high
        while True:
            while arr[i]<s:
                i+=1
            while arr[j]>s:
                j-=1
            if i>=j:
                return j
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

    def recursion(arr,low,high):
        if low<high:
            p=partition(arr,low,high)
            recursion(arr,p+1,high)
            recursion(arr,low,p)

        return arr
    
    recursion(numbers, 0, len(numbers) - 1)

def python_sort(lst):
	lst.sort()
