import sys

n = int(sys.stdin.readline().rstrip())

def print_star(n):
    if n == 0:
        return
    for _ in range(n):
        print("*", end=' ')
    print()
    print_star(n-1)
    for _ in range(n):
        print("*", end=' ')
    print()

print_star(n)