import sys

# counts Greater Common Divisor using Euclid's algorithm

a, b = int(sys.argv[1]),int(sys.argv[2])

while(b!=0):
    
    if(a<b):
        a,b=b,a
    
    a,b = b,a%b

print(a)