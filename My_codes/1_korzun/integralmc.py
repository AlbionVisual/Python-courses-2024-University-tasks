import sys, math

# calculates average function's (integral(sin(x)/x)) value using Monte Carlo method

a, b, n = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])

sum = 0
step = (b - a) / n

for i in range(n):
    if (a + i * step != 0):
        sum += math.sin(a + i * step)/(a + i * step)

answer = (b-a)/n * sum

print (answer)