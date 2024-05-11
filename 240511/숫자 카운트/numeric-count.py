import sys

# 모든 경우의 수를 저장하기 위한 집합
case = set()

# 모든 경우의 수 저장
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and j != k and k != i:
                case.add((i, j, k))

# 입력
n = int(sys.stdin.readline().rstrip())

# 각 입력에 대하여 가능성이 있는 경우의 수 탐색
for _ in range(n):
    test, ans_s, ans_b = sys.stdin.readline().rstrip().split()
    result = set()
    # 전체 경우의 수에 대하여
    for num in case:
        strike, ball = 0, 0
        for j in range(3):
            # 같은 자리 수에 위치하는지 확인
            if str(num[j]) == test[j]:
                strike += 1
            # 해당 자리 수가 존재하는지 확인
            elif str(num[j]) in test:
                ball += 1
        # 스트라이크와 볼이 정답과 동일할 경우
        if strike == int(ans_s) and ball == int(ans_b):
            # 가능성이 있는 수를 집합에 추가
            result.add(num)

    # N번의 탐색마다 가능성이 있는 전체 경우의 수를 업데이트
    case = result

print(len(result))