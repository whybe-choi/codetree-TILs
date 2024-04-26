n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False for _ in range(n+1)]

count = 0

def dfs(v):
    global count 
    for curr_v in range(1, n+1):
        if graph[v][curr_v] and not visited[curr_v]:
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)

print(count)