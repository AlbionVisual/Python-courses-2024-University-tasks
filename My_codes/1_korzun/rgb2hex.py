import sys

# Translate rgb to hex

a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
if a >= 255:
    a = 255
if b >= 255:
    b = 255
if c >= 255:
    c = 255

s = '#'

for i in [a // 16, a % 16, b // 16, b % 16, c // 16, c % 16]:

    if i < 10:
        s += str(i)
    elif i == 10:
        s += 'A'
    elif i == 11:
        s += 'B'
    elif i == 12:
        s += 'C'
    elif i == 13:
        s += 'D'
    elif i == 14:
        s += 'E'
    elif i == 15:
        s += 'F'

print(s)