import sys

c = float(sys.argv[1])

t = c
eps = 1e-15

while abs(t-c/t) > eps:
    t=(t+c/t)/2.0

print(t)