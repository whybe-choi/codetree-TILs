import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

seq = list(map(int, sys.stdin.readline().rstrip().split()))

max_sum = 0
for i in range(n-k+1):
    sum_k = sum(seq[i:i+k])
    max_sum = max(max_sum, sum_k)

print(max_sum)