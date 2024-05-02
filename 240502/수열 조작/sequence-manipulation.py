from collections import deque
import sys

n = int(sys.stdin.readline().strip())
seq = deque([i for i in range(1, n+1)])

while len(seq) != 1:
    # 1. 맨 앞의 정수를 제거합니다.
    seq.popleft()
    # 2. 남은 수열의 맨 앞의 정수를 맨 뒤로 이동
    seq.append(seq.popleft())

print(seq[0])