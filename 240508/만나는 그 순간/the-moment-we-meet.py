import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a, b = [0], [0]

# a
for _ in range(n):
    d, t = sys.stdin.readline().rstrip().split()
    t = int(t)
    if d == "L":
        for _ in range(t):
            a.append(a[-1]-1)
    else:
        for _ in range(t):
            a.append(a[-1]+1)

# b
for _ in range(m):
    d,t = sys.stdin.readline().rstrip().split()
    t = int(t)
    if d == "L":
        for _ in range(t):
            b.append(b[-1]-1)
    else:
        for _ in range(t):
            b.append(b[-1]+1)

min_len = min(len(a), len(b))

for i in range(1, min_len+1):
    if a[i] == b[i]:
        print(i)
        break