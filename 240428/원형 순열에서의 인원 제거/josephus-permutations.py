from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n+1))

while queue:
    queue.rotate(-(k-1))
    print(queue.popleft(), end=' ')