n = int(input())
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

max_coin = 0

for row in range(n):
    for col in range(n):
        if col + 2 >= n or row + 2 >= n:
            continue

        num_coin = 0

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                num_coin += grid[r][c]

        max_coin = max(max_coin, num_coin)

print(max_coin)