import sys
import matplotlib.pyplot as plt

def hilbert(n, s = 'L'):
    if n == 0: return s
    s = s.replace('L', '+rF-lFl-Fr+').replace('R', '-lF+rFr+Fl-')
    s = s.replace('r', 'R').replace('l', 'L').replace('+-', '').replace('-+', '')
    return hilbert(n - 1, s)

def graph(n):
    
    x = [0]
    y = [0]
    v = [1,0]
    
    for i in hilbert(n).replace('R','').replace('L',''):
        if i == '+': v[0], v[1] = -v[1], v[0]

        elif i == '-': v[0], v[1] = v[1], -v[0]

        elif i == 'F': 
            x.append(v[0] + x[-1])
            y.append(v[1] + y[-1])

    plt.plot(x, y, 'b')
    plt.show()
    
graph(int(sys.argv[1]))