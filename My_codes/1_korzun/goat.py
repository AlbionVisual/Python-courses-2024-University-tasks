import sys, math

x1 = R = float(sys.argv[1])
eps = float(sys.argv[2])
x2 = 2 * R

while (abs(x1 - x2) > eps):

    asin = math.asin(0.5 * x1 / R)
    F = (math.pi * (R**2 - x1**2) / 2.0) + (x1**2 * asin) - (2.0 * R**2 * asin) + (R**2 * math.sin(2.0 * asin))
    dF = x1 * (-math.pi + 2.0 * asin)

    x2, x1 = x1,x1 - F / dF

    

print(x2)