n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y, k):
    global num_block
    # 상, 하, 좌, 우
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if (new_x >= 0 and new_x < n) and (new_y >= 0 and new_y < n) and board[new_x][new_y] == k and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            num_block += 1
            dfs(new_x, new_y, k)

count = 0
max_block = 0 

for x in range(n):
    for y in range(n):
        # 같은 숫자로 이루어져 있는 경우 하나의 블럭으로 생각
        k = board[x][y]
        num_block = 0
        if not visited[x][y]:
            visited[x][y] = True
            num_block += 1
            dfs(x, y, k)
        
        if num_block >= 4:
            count += 1
        
        max_block = max(max_block, num_block)

print(count, max_block)