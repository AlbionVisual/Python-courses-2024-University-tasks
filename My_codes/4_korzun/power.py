import sys

def power(a, n):
    if n == 1: return a
    elif n == 0: return 1
    elif n % 2 == 0: return power(a, n//2) * power(a, n//2)
    else: return power(a, n//2) * power(a, n//2) * a

print(power(int(sys.argv[1]), int(sys.argv[2])))