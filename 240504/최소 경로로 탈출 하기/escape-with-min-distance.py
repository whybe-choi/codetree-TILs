import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

visited = [[-1 for _ in range(m)] for _ in range(n)]

def dfs():
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and grid[new_x][new_y] and visited[new_x][new_y] == -1:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[x][y] + 1

queue = deque()
queue.append((0, 0))
visited[0][0] = 0
dfs()
print(visited[n-1][m-1])