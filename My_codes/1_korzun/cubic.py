import sys, math

# solving equotation x^3+a*x^2+b*x+c=0 using Vieta formulas

a,b,c = float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])

Q = (a**2 - 3 * b) / 9
R = (2 * a**3 - 9 * a * b + 27 * c) / 54
S = Q**3 - R**2

if (S > 0):
    phi = math.acos(R/math.sqrt(Q**3))
    x_1 = -2 * math.sqrt(Q) * math.cos(phi) - a / 3
    x_2 = -2 * math.sqrt(Q) * math.cos(phi + 2 * math.pi / 3) - a / 3
    x_3 = -2 * math.sqrt(Q) * math.cos(phi - 2 * math.pi / 3) - a / 3

    print(x_1, x_2, x_3)

elif (S < 0):
    if (Q != 0):
        phi = math.acosh(abs(R)/math.sqrt(abs(Q)**3)) / 3
        x_1 = math.sqrt(abs(Q)) * (1 if R > 0 else -1 if R < 0 else 0) * math.cosh(phi) * (-2) - a / 3
        x_2 = math.sqrt(abs(Q)) * (1 if R > 0 else -1 if R < 0 else 0) * math.cosh(phi) - a / 3 + 1j * math.sqrt(3 * abs(Q)) * math.sinh(phi)
        x_3 = math.sqrt(abs(Q)) * (1 if R > 0 else -1 if R < 0 else 0) * math.cosh(phi) - a / 3 - 1j * math.sqrt(3 * abs(Q)) * math.sinh(phi)

    else:
        x_1 = -math.cbrt(c - a**3 / 27) - a / 3
        x_2 = - (a + x_1) / 2 + 1j/2 * math.sqrt(abs((a - 3 * x_1) * (a + x_1) - 4 * b))
        x_3 = - (a + x_1) / 2 - 1j/2 * math.sqrt(abs((a - 3 * x_1) * (a + x_1) - 4 * b))
    
    print(x_1, x_2, x_3)

else:
    x_1 = -2 * (1 if R > 0 else -1 if R < 0 else 0) * math.sqrt(Q) - a / 3
    x_2 = x_3 = (1 if R > 0 else -1 if R < 0 else 0) * math.sqrt(Q) - a / 3

    print(x_1, x_2, x_3)