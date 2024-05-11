import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())

# 서로 다른 숫자 세 개로 구성된 모든 세 자리 수
perms = list(permutations(range(1, 10), 3))

# 불가능한 세 자리 수의 모음
impossible = []

# N번의 입력에 대하여
for _ in range(n):
    num, count_1, count_2 = sys.stdin.readline().rstrip().split()
    count_1, count_2 = int(count_1), int(count_2)

    # 모든 경우의 수에 대하여
    for perm in perms:
        # 정답 카운트와 비교하기 위한 카운트
        c1, c2 = 0, 0
        # 각 자리 수에 대하여
        for i in range(3):
            # 해당 자리 수가 특정 세 자리 수에 존재하며
            if int(num[i]) in perm:
                # 해당 자리 수가 동일한 자리에 위치한다면
                if int(num[i]) == perm[i]:
                    # 1번 카운트가 하나 올라가고
                    c1 += 1
                # 그렇지 않다면, 즉 존재하지만 동일한 자리 수는 아닐 경우
                else:
                    # 2번 카운트가 하나 올라간다
                    c2 += 1
        
        # 특정 경우의 수에 대하여 정답 카운트와 같지 않다면
        if count_1 != c1 or count_2 != c2:
            # 가능성이 없는 수 + 1
            impossible.append(perm)

    

# 전체 경우의 수에서 가능성이 없는 경우의 수를 제외하면 유추할 가능성이 있는 수의 총 개수가 나온다
# N번 반복하여 전체 경우의 수를 탐색할 경우 가능성이 없는 경우의 수가 중복이 될 수 있기 때문에 이를 유의해야한다.
print(len(perms) - len(set(impossible)))