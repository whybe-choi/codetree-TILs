from collections import deque

queue = deque()

n = int(input())

for _ in range(n):
    command = input()

    if command.startswith('push'):
        queue.append(int(command.split()[1]))
    elif command.startswith('pop'):
        print(queue.popleft())
    elif command.startswith('size'):
        print(len(queue))
    elif command.startswith('empty'):
        print(1 if len(queue) == 0 else 0)
    else:
        print(queue[0])