import sys

n = int(sys.stdin.readline().rstrip())

dp = [-1 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)