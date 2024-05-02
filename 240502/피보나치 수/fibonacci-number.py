import sys

n = int(sys.stdin.readline().rstrip())

dp = [-1 for _ in range(45)]

# 초기값
dp[0] = 1
dp[1] = 1

for i in range(2, 45):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])