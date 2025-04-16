import sys 

arr = [int(s) for s in sys.argv[1]]
print (arr)


while len(arr) > 1:
    arr = [int(s) for s in str(sum(arr))]
    print (arr)