import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

score = [0 for _ in range(10001)]

for _ in range(n):
    loc, alpha = sys.stdin.readline().rstrip().split()
    score[int(loc)] = 1 if alpha == "G" else 2

max_score = 0
for i in range(1, 10000-k+1):
    sum_score = sum(score[i:i+k+1])
    max_score = max(max_score, sum_score)

print(max_score)