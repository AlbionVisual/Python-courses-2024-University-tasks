import sys

def isInvalidInput(arrs):

    for i in range(len(arrs) - 1):
        if len(arrs[i+1]) != len(arrs[i][0]):
            return 'Error: incompatible sizes of matrices'
    
    return False

def multiplyMatrices(matr1, matr2):
    result = [[0 for i in range(len(matr2[0]))] for j in range(len(matr1))]
    for i in range(len(matr1)):
        for j in range(len(matr2[0])):
            for k in range(len(matr2)):
                result[i][j] += matr1[i][k] * matr2[k][j]
            
    return result

if len(sys.argv) <= 1:
    print('Error: invalid input')
else:
    matrices = sys.argv[1:]
    matrices = [i.split(',') for i in matrices]
    matrices = [[i.split(' ') for i in j] for j in matrices]
    matrices = [[[float(i) for i in j] for j in k] for k in matrices]

    error = isInvalidInput(matrices)
    if error:
        print(error)
    else:
        result = matrices[0]
        for i in range(1, len(matrices)):
            result = multiplyMatrices(result, matrices[i])
        print(result)
