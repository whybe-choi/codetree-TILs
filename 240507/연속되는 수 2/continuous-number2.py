import sys

n = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

base = nums[0]
count = 1
for i in range(1, n):
    if base == nums[i]: 
        count += 1
    else:
        base = nums[i]

print(count)