import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(n-m+1):
    if Counter(a[i:i+m]) == Counter(b):
        count += 1

print(count)