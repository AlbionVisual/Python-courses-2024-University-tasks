import sys, math

a, b, n = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])

def f(x):
    return math.atan(x) / x if x != 0 else 0

def basicIntegral(x1, x2, count, f):

    delta = (x2 - x1) / count

    rightSum = sum([f(x1 + delta * i) for i in range(1, count)])
    leftSum = rightSum + f(x1)
    rightSum += f(x2)

    midSum = sum([f(x1 + delta * (2 * i + 1) / 2) for i in range(count)])
    return leftSum * delta, rightSum * delta, midSum * delta

def trapIntegral(x1,x2,count, f):

    delta = (x2 - x1) / count
    
    trapSum = sum([(f(x1 + delta * i) + f(x1 + delta * (i + 1))) * (x1 + delta * (i + 1) - x1 - delta * i) / 2 for i in range(n)])
    
    return trapSum

def simpsonIntegral(x1,x2,count, f):

    count *= 2
    delta = (x2 - x1) / count

    simpSum = sum([f(x1 + delta * (i-1)) + 4 * f(x1 + delta * i) + f(x1 + delta * (i + 1)) for i in range(1, count, 2)])

    return simpSum * delta / 3


print("Left: \t\t" + str(basicIntegral(a,b,n, f)[0]))
print("Right:\t\t" + str(basicIntegral(a,b,n, f)[2]))
print("Mid:  \t\t" + str(basicIntegral(a,b,n, f)[1]))
print("Trap: \t\t" + str(trapIntegral(a,b,n, f)))
print("Simps:\t\t" + str(simpsonIntegral(a,b,n, f)))