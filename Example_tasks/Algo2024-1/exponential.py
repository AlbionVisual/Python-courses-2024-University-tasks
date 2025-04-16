import sys, math

# calc:
# exp (x) = 1 + x + x^2/2! + x^3/3! + ...

x = float(sys.argv[1])
eps = 1e-15

elem = x
y = 1 + elem

i = 2
while True:
    elem = elem * x / i
    if (elem < eps):
        break
    else:
        y = y + elem
        i = i + 1

print(y)
print(math.exp(x))