from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def dfs():
    global count
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < n) and grid[new_x][new_y] == 0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                # 방문 횟수 1 증가
                count += 1
                queue.append((new_x, new_y))

# 방문 횟수
count = 0

for _ in range(k):
    r, c = map(int, input().split())
    queue = deque()
    # 모든 시작점의 위치에 적혀있는 숫자는 0이므로 방문 가능
    queue.append((r-1, c-1))
    visited[r-1][c-1] = True
    count += 1
    dfs()

print(count)