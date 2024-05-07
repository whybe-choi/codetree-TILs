import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

MIN_SUM = sys.maxsize
for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = abs(i - j) * a[j]
        sum_dist += dist
    MIN_SUM = min(MIN_SUM, sum_dist)
        
print(MIN_SUM)