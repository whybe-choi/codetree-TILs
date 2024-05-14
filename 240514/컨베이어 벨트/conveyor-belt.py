import sys

n, t = map(int, sys.stdin.readline().rstrip().split())

grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]

for _ in range(t):
    # 위 변에 있는 마지막 숫자 저장
    temp1 = grid[0][n-1]
    # 위 변에 있는 숫자 오른쪽으로 밀기
    for i in range(n-1, 0, -1):
        grid[0][i] = grid[0][i-1]
    # 아래 변에 있는 마지막 숫자 저장
    temp2 = grid[1][n-1]
    # 아래 변에 있는 숫자 오른쪽으로 밀기
    for j in range(n-1, 0, -1):
        grid[1][j] = grid[1][j-1]
    # 위 변에 있는 첫번째 숫자를 아래 변에 있는 첫번째 숫자로 바꾸기
    grid[0][0] = temp2
    # 아래 변에 있는 마지막 숫자를 위 변에 있는 마지막 숫자로 바꾸기
    grid[1][0] = temp1

for row in grid:
    print(*row)