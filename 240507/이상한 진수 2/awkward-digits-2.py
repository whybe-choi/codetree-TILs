import sys

a = sys.stdin.readline().rstrip()

max_n = 0
for i in range(1, len(a)):
    if a[i] == "0":
        temp = a[:i] + "1" + a[i+1:]
    max_n = max(max_n, int(temp, 2))

print(max_n)