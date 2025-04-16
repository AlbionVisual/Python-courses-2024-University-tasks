import sys

# Searching for modas

if len(sys.argv) > 1:
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

    if sum(frequency) == len(nums):
        print([])
    else:
        max = 0
        for val in frequency:
            if val > max:
                max = val
        res = []
        for i in range(len(nums)):
            if frequency[i] == max:
                res.append(nums[i])
        print(res)
else:
    print([])