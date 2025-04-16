import sys, random

# calc pi using Monte-Carlo method

n = int(sys.argv[1])

square = 0
circle = 0

for i in range(n):
    x = random.random()
    y = random.random()
    square += 1
    if (x*x + y*y <= 1):
        circle += 1

print(4 * circle / square)