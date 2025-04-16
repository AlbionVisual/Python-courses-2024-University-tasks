import sys

matr = sys.argv[1]

matr = matr.split(',')
matr = [i.strip() for i in matr]
matr = [i.split(' ') for i in matr]
matr = [[float(j) for j in i] for i in matr]

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

    


print(matr)