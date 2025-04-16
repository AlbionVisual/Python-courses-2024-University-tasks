import sys, time

# facto n, e. g. 36 = 2 * 2 * 3 * 3 without unnecessary calculates

n = int(sys.argv[1])

factor = 2
s = ''

start = time.time()
while (n > 1 and factor**2 <= n):
    
    while (n % factor == 0):
        print(factor)
        
        s += str(factor) + ' '
        n //= factor
    factor += 1

if (n > 1):
    s += str(n) + ' '

end = time.time()

print(s)

print(end - start)