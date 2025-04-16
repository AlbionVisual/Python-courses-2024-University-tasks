import sys

# checks wether number leap year or not

y = int(sys.argv[1])

print(str(y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)))