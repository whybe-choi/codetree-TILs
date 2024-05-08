import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())

fine = [0 for _ in range(n+1)]

answer = -1
for _ in range(m):
    student = int(sys.stdin.readline().rstrip())
    fine[student] += 1
    if fine[student] >= k:
        answer = student

print(answer)