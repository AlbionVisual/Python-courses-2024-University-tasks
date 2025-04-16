import sys

arr = sys.argv[1]
arr = arr.split(',')
arr = sorted([int(i) for i in arr])

nums = []
frequency = []
for i in arr:
    if i in nums:
        j = 0
        while nums[j] != i:
            j += 1
        frequency[j] += 1
    else:
        nums.append(i)
        frequency.append(1)

mas = [[nums[i],frequency[i]] for i in range(len(nums))]
print(mas)