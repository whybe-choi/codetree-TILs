import sys

n = int(sys.stdin.readline().rstrip())

grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

# 초기값
# (0, 0)
dp[0][0] = grid[0][0]

# 0행에 있는 값
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# 0열에 있는 값
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# DP table 채우기
# 오른쪽으로 이동한 경우와 밑으로 이동한 경우 중 숫자의 합이 최대가 되는 값을 DP table에 저장
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

print(dp[n-1][n-1])