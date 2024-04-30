from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

queue = deque()

def dfs():
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        # queue에서 현재 위치 추출
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < m) and grid[new_x][new_y] and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))

# root에 대해서 방문 처리
visited[0][0] = 1
queue.append((0, 0))

dfs()
print(visited[n-1][m-1])