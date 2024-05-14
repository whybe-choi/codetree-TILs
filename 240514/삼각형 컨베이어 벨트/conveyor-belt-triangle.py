import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
left = list(map(int, sys.stdin.readline().rstrip().split()))
right = list(map(int, sys.stdin.readline().rstrip().split()))
down = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(t):
    # 삼각형의 왼쪽 위 변에 있는 마지막 숫자 저장
    temp1 = left[-1]
    # 삼각형 왼쪽 위 변에 있는 숫자들 오른쪽으로 밀기
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]
    # 삼각형의 오른쪽 위 변에 있는 마지막 숫자 저장
    temp2 = right[-1]
    # 삼각형 오른쪽 위 변에 있는 숫자들 오른쪽으로 밀기
    for i in range(n-1, 0, -1):
        right[i] = right[i-1]
    # 삼각형의 아래 변에 있는 마지막 숫자 저장
    temp3 = down[-1]
    # 삼각형 아래 변에 있는 숫자들 오른쪽으로 밀기
    for i in range(n-1, 0, -1):
        down[i] = down[i-1]
    # 삼각형의 왼쪽 위 변에 있는 마지막 숫자를 오른쪽 위 변에 있는 첫번째 숫자로 저장
    right[0] = temp1
    # 삼각형의 오른쪽 위 변에 있는 마지막 숫자를 아래 변에 있는 첫번째 숫자로 저장
    down[0] = temp2
    # 삼각형의 아래 변에 있는 마지막 숫자를 왼쪽 위 변에 있는 첫번째 숫자로 저장
    left[0] = temp3

print(*left)
print(*right)
print(*down)