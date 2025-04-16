import sys, math

# calculates number Pi using one of three algorithms

accuracy, type = float(sys.argv[1]), str(sys.argv[2])

x=0
i=-1
delta = 100

if (type=='leibniz'):
    while (4 * abs(delta) > accuracy):
        i = i + 1
        delta = (-1)**i/(2*i+1)
        x += delta
    print(str(i), str(4*x))
elif (type=='pairwise'):
    while (4 * abs(delta) > accuracy):
        i=i+1
        delta = 1/(4*i+1)-1/(4*i+3)
        x = x + delta
    print(str(i), str(4*x))
elif (type=='bbp'):
    while (abs(delta) > accuracy):
        i = i + 1
        delta = 1/(16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
        x = x + delta
    print(str(i), str(x))