import sys

# converting array of numbers to avg geometric, avg algebric, median and avg squared            )

arr = sys.argv[1]
arr = arr.split(',')
arr = sorted([int(i) for i in arr])

res = [1, 0, 0, 0]

for i in arr:
    res[0] *= i

res[0] = pow(res[0], 1 / len(arr))

res[1] = sum(arr) / len(arr)

res[2] = (arr[int(len(arr) / 2 - 0.5)] + arr[int(len(arr) / 2)]) / 2

arr = [i**2 for i in arr]
res[3] = pow(sum(arr) / len(arr),1 / 2)

res = [float(int(i * 100 + 0.5)) / 100 for i in res]

print(res)