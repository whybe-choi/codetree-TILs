from collections import deque

n =  int(input())

d = deque()
for _ in range(n):
    command = input()
    if command.startswith("push_front"):
        a = int(command.split()[-1])
        d.appendleft(a)
    elif command.startswith("push_back"):
        a = int(command.split()[-1])
        d.append(a)
    elif command.startswith("pop_front"):
        print(d.popleft())
    elif command.startswith("pop_back"):
        print(d.pop())
    elif command.startswith("size"):
        print(len(d))
    elif command.startswith("empty"):
        print(0 if d else 1)
    elif command.startswith("front"):
        print(d[0])
    else:
        print(d[-1])