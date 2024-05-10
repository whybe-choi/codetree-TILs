import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(n-m+1):
    exists = True
    for j in range(m):
        if b[j] not in a[i:i+m]:
            exists = False

    if exists:
        count += 1

print(count)