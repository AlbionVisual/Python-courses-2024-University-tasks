import sys

def spiralmatrix(size):

    def numbers():
        i = 1
        while True: yield str(i); i += 1
    num = numbers()

    def recursion(n):
        if n == 1: return [[next(num)]]
        if n == 0: return
        assert n > 0, 'n must be bigger than 0'
        
        matr = [[0] * n for _ in range(n)]
        for i in range(n):
            matr[0][i] = next(num)
        for i in range(1, n):
            matr[i][n-1] = next(num)
        for i in range(1, n):
            matr[n-1][n - 1 - i] = next(num)
        for i in range(1, n - 1):
            matr[n - 1 - i][0] = next(num)
        submatr = recursion(n - 2)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                matr[i][j] = submatr[i - 1][j - 1]
        return matr

    return recursion(size)


matr = spiralmatrix(int(sys.argv[1]))
for line in matr:
    print('\t'.join(line))
