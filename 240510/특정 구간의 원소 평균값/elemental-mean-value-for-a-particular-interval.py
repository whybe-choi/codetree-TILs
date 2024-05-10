import sys

n = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        avg = sum(seq[i:j+1]) / (j-i+1)
        if avg in seq[i:j+1]:
            count += 1

print(count)