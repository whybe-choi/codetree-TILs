import sys

n = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = 0
max_cnt = 0
for i in range(n):
    if i > 0 and arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt = 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)