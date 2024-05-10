import sys

max_loc = 100

n, k = map(int, sys.stdin.readline().rstrip().split())
bucket = [0 for _ in range(max_loc+1)]

for _ in range(n):
    candy, idx = map(int, sys.stdin.readline().rstrip().split())
    bucket[idx] += candy

max_candy = 0
for i in range(max_loc - 2*k + 1):
    sum_candy = sum(bucket[i:i+2*k+1])
    max_candy = max(max_candy, sum_candy)

print(max_candy)