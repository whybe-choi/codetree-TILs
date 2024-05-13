import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cases = []

# 가능한 블럭 종류는 총 6개
# [dx1, dx2]
# [dy1, dy2]
dxs = [[0, 1], [0, 1], [-1, 0], [-1, 0], [-1, 1], [0, 0]]
dys = [[-1, 0], [1, 0], [0, 1], [0, -1], [0, 0], [-1, 1]]

for x in range(n):
    for y in range(m):
        for dx, dy in zip(dxs, dys):
            if (0 <= x+dx[0] < n) and (0 <= x+dx[1] < n) and (0 <= y+dy[0] < m) and (0 <= y+dy[1] < m):
                cases.append(grid[x][y] + grid[x+dx[0]][y+dy[0]] + grid[x+dx[1]][y+dy[1]])

print(max(cases))