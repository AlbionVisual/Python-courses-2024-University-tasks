import sys
import matplotlib.pyplot as plot

n = int(sys.argv[1])
x = []
y = []
i = 0
max = n
maxId = 0

while n != 1:
    x.append(i)
    y.append(n)
    if n % 2 == 0: n //= 2
    else: n = 3 * n + 1
    i += 1
    if max < n: 
        max = n
        maxId = i

plot.title('Последовательность 3n + 1')
plot.plot(x,y)
plot.plot(maxId, max, 'r')

plot.show()