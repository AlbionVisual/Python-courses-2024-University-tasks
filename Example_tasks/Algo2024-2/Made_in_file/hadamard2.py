import sys, math

# Generates Hadamard matrix of size n
# h1 = [[1]]
# h2 = [[h1 h1], [h2 not(h1)]]
# h4 = [[h2 h2], [h2 not(h2)]]

def hadamard_matrix(size):
    n = int(math.log(size, 2))
    h = [[0] * size for i in range(size)]
    h[0][0] = 1
    for k in range(n):
        for i in range(2**k):
            for j in range(2**k):
                h[i][j+2**k] = h[i][j]
                h[i+2**k][j] = h[i][j]
                h[i+2**k][j+2**k] = -h[i][j]
    return h

def transposed_matrix(matr):
    size = len(matr)
    tmatr = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            tmatr[i][j] = matr[j][i]
    return tmatr

def matrix_product(matr1, matr2):
    size = len(matr1)
    prod = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                prod[i][j] += matr1[i][k] * matr2[k][j]
    return prod
def show_matrix(matr):
    size = len(matr)
    for i in range(size):
        s=''
        for j in range(size):
            s += str(matr[i][j]) + '\t'
        print(s)

size = int(sys.argv[1])
h = hadamard_matrix(size)

show_matrix(matrix_product(
    hadamard_matrix(size),
    transposed_matrix(h)
))