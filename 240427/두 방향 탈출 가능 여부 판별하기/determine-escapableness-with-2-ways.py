n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < m)

def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and grid[new_x][new_y] and not visited[new_x][new_y]:
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)
    

visited[0][0] = 1
dfs(0, 0)
print(1 if visited[n-1][m-1] == 1 else 0)