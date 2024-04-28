n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < m)

def dfs(x, y, k):
    # 하, 우, 상, 좌
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and grid[new_x][new_y] > k and not visited[new_x][new_y]:
            visited[new_x][new_y] = 1
            dfs(new_x, new_y, k)

# k의 최댓값
max_k = 0

for row in range(n):
    for col in range(m):
        if grid[row][col] > max_k:
            max_k = grid[row][col]

# k값에 따른 안전 영역의 수
safe_zone = []

for k in range(1, max_k+1):
    # 가능한 k값마다 visited를 초기화해줘야 함.
    visited = [[0 for _ in range(m)] for _ in range(n)]
    # 안전 영역의 수
    count = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] > k and not visited[x][y]:
                count += 1
                visited[x][y] = 1
                dfs(x, y, k)

    safe_zone.append([count, k])

print(*sorted(safe_zone, key=lambda x: (x[0], -x[1]))[-1])