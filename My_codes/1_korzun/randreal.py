import random, sys

# generates random real number that located in a given segment

floor, ceiling = int(sys.argv[1]),int(sys.argv[2])

print(str(floor + (ceiling - floor) * random.random()))