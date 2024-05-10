import sys

n, h, t = map(int, sys.stdin.readline().rstrip().split())

heights = list(map(int, sys.stdin.readline().rstrip().split()))

min_diff = sys.maxsize
for i in range(n-t+1):
    sum_diff = 0
    for j in range(i, i+t):
        sum_diff += abs(h-heights[j])

    min_diff = min(min_diff, sum_diff)

print(min_diff)