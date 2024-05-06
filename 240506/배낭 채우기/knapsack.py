import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

bag = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    bag.append([w, v])

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j >= bag[i-1][0]:
            dp[i][j] = max(dp[i-1][j-bag[i-1][0]]+bag[i-1][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
print(dp[n][m])