import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def selection_sort(arr):
    for i in range(n-1):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                arr[j], arr[minimum] = arr[minimum], arr[j]
                
    return arr

sorted_arr = selection_sort(arr)
print(*sorted_arr)