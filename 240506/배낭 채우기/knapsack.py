import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

weights, values = [], []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(m+1)] for _ in range(n)]

# 초기값
dp[0][weights[0]] = values[0]

for i in range(1, n):
    for j in range(m+1):
        if j >= weights[i]:
            dp[i][j] = max(dp[i-1][j-weights[i]]+values[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]


# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
max_value = -1
for i in range(n):
    for j in range(m+1):
        max_value = max(dp[i][j], max_value)

print(max_value)