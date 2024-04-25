x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

n = int(input())
for i in range(n):
    dir, num = input().split()
    if dir == "W":
        x, y = x+dx[0]*int(num), y+dy[0]
    elif dir == "S":
        x, y = x+dx[1], y+dy[1]*int(num)
    elif dir == "N":
        x, y = x+dx[2], y+dy[2]*int(num)
    else:
        x, y = x+dx[3]*int(num), y+dy[3]

print(x, y)