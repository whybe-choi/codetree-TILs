import sys

n = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(1001)]

dp[0] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 1001):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n] % 10007)