import sys

n = int(sys.stdin.readline().rstrip())

cow = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cow[i] <= cow[j] and cow[j] <= cow[k]:
                count += 1

print(count)