import sys

max_loc = 100

n, k = map(int, sys.stdin.readline().rstrip().split())
bucket = [0 for _ in range(max_loc+1)]

for _ in range(n):
    candy, idx = map(int, sys.stdin.readline().rstrip().split())
    bucket[idx] += candy

max_candy = 0
for c in range(max_loc+1):
    left = c-k if c-k > 0 else 0
    right = c+k if c+k < max_loc else max_loc
    sum_candy = sum(bucket[left:right+1])
    max_candy = max(max_candy, sum_candy)


print(max_candy)