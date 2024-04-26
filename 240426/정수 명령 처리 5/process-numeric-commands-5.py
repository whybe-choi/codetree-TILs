n = int(input())
arr = []

for _ in range(n):
    order = list(input().split())

    if order[0] == 'size':
        print(len(arr))
    elif order[0] == 'pop_back':
        arr.pop()
    elif order[0] == 'get':
        print(arr[int(order[1])-1])
    else:
        arr.append(int(order[1]))