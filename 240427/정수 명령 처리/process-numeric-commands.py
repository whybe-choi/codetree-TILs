n = int(input())

stack = []

for _ in range(n):
    command = input()

    if command.startswith("push"):
        _, a = command.split()
        stack.append(int(a))
    elif command.startswith("pop"):
        n = stack.pop()
        print(n)
    elif command.startswith("size"):
        print(len(stack))
    elif command.startswith("empty"):
        print(1 if len(stack) == 0 else 0)
    else:
        print(stack[-1])