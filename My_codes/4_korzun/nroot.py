from sys import argv as entries

def nroot_nuton(n, k, eps):

    def f(x, n, k): return (x**k - n)
    def df(x, k): return (k * x**(k-1))
    
    x0 = n / 4
    x1 = n / 2
    x2 = n
    i = 0
    # while abs((x2 - x1)/(1-(x2 - x1)/(x1 - x0))) > eps:
    while abs(x2 - x1) > eps:
        x0 = x1
        x1, x2 = x2, x2 - f(x2, n, k) / df(x2, k)
        i += 1
        # print(x1)
    
    return i, x2

def nroot_binary(n, k, eps):

    i = 0
    f = lambda x: x**k
    def recursion(min, max):
        nonlocal i
        i += 1
        mid = max - (max - min) / 2
        # print(mid)
        if abs(min - max) < eps: return mid
        elif f(mid) < n: return recursion(mid, max)
        elif f(mid) > n: return recursion(min, mid)
        elif f(mid) == n: return mid

    res = recursion(0, n)
    return i, res

if len(entries) == 1: n, k, eps = 2, 2, 0.01
elif len(entries) == 2: n, k, eps = entries[1], 2, 0.01
elif len(entries) == 3: n, k, eps = entries[1], entries[2], 0.01
else: n, k, eps = [float(i) for i in entries[1:]]

binary_n, binary_ans = nroot_binary(n, k, eps)
nuton_n, nuton_ans = nroot_nuton(n, k, eps)

print(binary_n, binary_ans)
print(nuton_n, nuton_ans)
# print(f'Ans {n**(1/k)}')