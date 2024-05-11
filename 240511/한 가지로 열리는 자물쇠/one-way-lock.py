import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))

count = n ** 3
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(i - num[0]) > 2 and abs(j - num[1]) > 2 and abs(k - num[2]) > 2:
                count -= 1

print(count)