import sys
from timeit import default_timer
file_name=sys.argv[1]

n = int(sys.argv[2])

W = int(sys.argv[3])

def read_file(file_name):
    v = [] #ценность
    w = []
    file = open(file_name,'r')
    for i in file.readlines():
        t = i.split()
        v.append(int(t[0]))
        w.append(int(t[1]))
    return v,w

def knapsack_greedy(v, w, W):
    mas = [(i,j) for i,j in zip(v,w)]
    mas.sort(key = lambda a: a[0]/a[1],reverse = True)

    value = 0
    cur_W = 0

    for i in mas:
        if cur_W + i[1] > W:
            continue
        value += i[0]
        cur_W += i[1]
    return value

# def knapsack_recursive(v, w, i, W):
#     if i < 0 or W == 0:
#         return 0
#     if w[i] > W:
#         return knapsack_recursive(v, w, i - 1, W)
#     else:
#         return max(knapsack_recursive(v, w, i - 1, W), v[i] + knapsack_recursive(v, w, i - 1, W - w[i]))


def knapsack_topdown(v, w, i, W, lookup):
    if i < 0 or W == 0:
        return 0
    if (i,W) in lookup:
        return lookup[(i,W)]
    if w[i] > W:
        res = knapsack_topdown(v, w, i - 1, W,lookup)
    else:
        res = max(knapsack_topdown(v, w, i - 1, W,lookup), v[i] + knapsack_topdown(v, w, i - 1, W - w[i],lookup))

    lookup[(i,W)] = res
    return res

def knapsack_bottomup(v, w, W):
    l = len(v)
    sack = [[0]*(W+1) for i in range(l)]


    for i in range(l):
        for j in range(1, W+1):
            if w[i] > j:
                sack[i][j] = sack[i-1][j]
            else:
                sack[i][j] = max(sack[i-1][j], v[i] + sack[i-1][j-w[i]])

    return sack[l-1][W]

v,w = read_file(file_name)
v = v[:n]
w = w[:n]
print(f'\nGreedy knapsack')
t0 = default_timer()
print(knapsack_greedy(v,w,W))
print(default_timer()-t0)

print(f'\nTop-down knapsack')
lookup = {}
t0=default_timer()
print(knapsack_topdown(v,w,len(v)-1,W,lookup))
print(default_timer()-t0)

print(f'\nBottom-up knapsack')
t0=default_timer()
print(knapsack_bottomup(v,w,W))
print(default_timer()-t0)