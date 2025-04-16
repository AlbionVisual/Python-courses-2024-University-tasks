import sys

n = int(sys.argv[1])
armstrong = []
for i in range(1,n):
    k = len(str(i))
    if sum([int(j)**k for j in list(str(i))]) == i:
        armstrong.append(i)

print(armstrong)