import sys

n = int(sys.stdin.readline().rstrip())
grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
r, c = map(int, sys.stdin.readline().rstrip().split())

# 해당 칸에 적힌 수 - 1만큼 인접한 격자도 터짐
num = grid[r-1][c-1]-1

# 터지는 격자의 위치를 boom 집합에 저장
boom = set()

for i in range(r-1-num, r+num):
    if 0 <= i < n:
        boom.add((i, c-1))

for j in range(c-1-num, c+num):
    if 0 <= j < n:
        boom.add((r-1, j))

# 터지고 떨어지는 경우를 저장하기 위한 배열
temp = [[0 for _ in range(n)] for _ in range(n)]

# 모든 열에 대하여 터지고 떨어지는 경우 생각하기
for col in range(n):
    # 해당 열의 가장 아래 행부터 비교하기
    temp_row = n-1
    for row in range(n-1, -1, -1):
        # 해당 (행, 열)이 폭발하는 위치에 존재하지 않으면
        if not (row, col) in boom:
            # 배열에 추가
            temp[temp_row][col] = grid[row][col]
            temp_row -= 1

# 매 행마다 출력하기
for row in temp:
    print(*row)