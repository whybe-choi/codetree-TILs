import sys

n = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

base = nums[0]
cnt = 1
max_cnt = 1
for i in range(1, n):
    if base == nums[i]: 
        cnt += 1
    else:
        base = nums[i]
        cnt = 1 
    max_cnt = max(max_cnt, cnt)

print(max_cnt)