import sys

n = int(sys.stdin.readline().rstrip())
arr = [i for i in range(n, 0, -1)]

def print_n(arr, i, n):
    if i >= n:
        return
    print(arr[i], end=' ')
    print_n(arr, i+1, n)
    print(arr[i], end=' ')

print_n(arr, 0, n)