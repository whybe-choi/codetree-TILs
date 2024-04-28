n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < n)

def dfs(x, y):
    global num
    # 하, 좌, 상, 우
    dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and grid[new_x][new_y] and not visited[new_x][new_y]:
            visited[new_x][new_y] = 1
            num += 1
            dfs(new_x, new_y)
            
count = 0   
people = []

for x in range(n):
    for y in range(n):
        num = 0
        if grid[x][y] and not visited[x][y]:
            count += 1
            visited[x][y] = 1
            num += 1
            dfs(x, y)
            people.append(num)

print(count)
for person in sorted(people):
    print(person)