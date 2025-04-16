import sys

# :(

def isValid(A, b):
    if len(A[0]) != len(b):
        return False
    return True

def calcEquo(eq, sol):
    i = 0
    while eq[i] == 0:
        i += 1
    sum = 0
    for j in range(len(sol)):
        sum += eq[i + 1 + j] * sol[-j - 1]
    
    return (eq[-1] - sum) / eq[i]

def echelonform(matr):
    for i in range(len(matr)):

        if matr[i][i] == 0:
            for j in range(i, len(matr)):
                if matr[j][i] != 0:
                    matr[j], matr[i] = matr[i], matr[j]
                    break
            else:
                continue
    
        for j in range(i+1, len(matr)):
            koff = matr[j][i] / matr[i][i]
            for k in range(i, len(matr[j][i:])+i):
                matr[j][k] -= matr[i][k] * koff
    
    return matr

if len(sys.argv) > 2:
    A, b = str(sys.argv[1]), str(sys.argv[2])
    A = A.split(',')
    A = [i.strip() for i in A]
    A = [i.split(' ') for i in A]
    A = [[int(i) for i in j] for j in A]
    b = b.split(',')
    b = [int(i) for i in b]

    if not(isValid(A,b)):
        print('Error: incompatible sizes of matrices')
        
    matr = A.copy()
    for i in range(len(b)):
        matr[i].append(b[i])
    
    matr = echelonform(matr)
    print(matr)
    solutions = []
    for i in range(len(matr)):
        eq = matr[(1 + i) * -1 ]
        amount = i + 2
        if sum([0 if i == 0 else 1 for i in eq]) != amount:
            solutions = []
            break
        
        solutions.append(calcEquo(eq, solutions))
        
        print(eq, solutions)

    if solutions != []:
        print([solutions[-i - 1] for i in range(len(solutions))])
    else:
        print('Error: no solution')
else:
    print('Error: invalid input')

