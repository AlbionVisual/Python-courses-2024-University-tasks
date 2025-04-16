import sys, math

b=float(sys.argv[1])
c=float(sys.argv[2])

d=math.sqrt(b**2-4*c)

if (d >= 0):
    print('x^2+'+str(sys.argv[1])+'x+'+str(sys.argv[2]))
    print('x1='+str((-b+d)/2))
    print('x2='+str((-b-d)/2))
else:
    print('d < 0')