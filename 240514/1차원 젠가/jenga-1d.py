import sys

n = int(sys.stdin.readline().rstrip())

jenga = [int(sys.stdin.readline().rstrip()) for _ in range(n)][::-1]

for _ in range(2):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    temp = [0 for _ in range(n)]
    temp_idx = 0
    for i in range(n):
        if not (i in range(s, e+1)):
            temp[temp_idx] = jenga[i]
            temp_idx += 1
    jenga = temp

count = 0
for block in jenga:
    if block != 0:
        count += 1
print(count)

for block in jenga[::-1]:
    if block != 0:
        print(block)