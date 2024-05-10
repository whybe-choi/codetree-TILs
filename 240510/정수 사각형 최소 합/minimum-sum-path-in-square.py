import sys

n = int(sys.stdin.readline().rstrip())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

# 초기값
# 1. (1, N)에서 시작
dp[0][n-1] = grid[0][n-1]

# 2. 첫번째 행의 값은 이전 위치가 해당 값의 오른쪽 값임.
for i in range(1, n):
    dp[0][n-1-i] = dp[0][n-i] + grid[0][n-1-i]

# 3. 가장 오른쪽 열의 값은 이전 위치가 해당 값의 위 값임.
for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

# DP table 채우기
for i in range(1, n):
    for j in range(2, n+1):
        dp[i][n-j] = min(dp[i-1][n-j], dp[i][n-j+1]) + grid[i][n-j]


print(dp[n-1][0])