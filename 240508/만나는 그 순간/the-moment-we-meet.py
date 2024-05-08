import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a, b = [0], [0]

# a
for _ in range(n):
    d, t = sys.stdin.readline().rstrip().split()
    for _ in range(int(t)):
        a.append(a[-1] + (1 if d == 'R' else -1)

# b
for _ in range(m):
    d, t = sys.stdin.readline().rstrip().split()
    for _ in range(int(t)):
        a.append(b[-1] + (1 if d == 'R' else -1)

min_len = min(len(a), len(b))

answer = -1
for i in range(1, min_len):
    if a[i] == b[i]:
        answer = i
        break

print(answer)