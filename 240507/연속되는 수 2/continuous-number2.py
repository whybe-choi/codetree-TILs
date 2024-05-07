import sys

n = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

base = nums[0]
count = 0
for i in range(n):
    if base == nums[i]: 
        count += 1
    else:
        base = nums[i]

print(count)