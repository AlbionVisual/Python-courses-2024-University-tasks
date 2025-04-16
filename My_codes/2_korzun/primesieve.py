import sys

n = int(sys.argv[1])

nums = [i for i in range(2, n+1)]
n-=1

primes = []
while nums:
    primes.append(nums[0])
    nums = [i for i in nums if i % nums[0] != 0]
    
print(primes)