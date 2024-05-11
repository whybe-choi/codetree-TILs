import sys

capa = list(map(int, sys.stdin.readline().rstrip().split()))

min_diff = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            team1 = capa[i] + capa[j] + capa[k]
            team2 = sum(capa) - team1
            min_diff = min(min_diff, abs(team1 - team2))

print(min_diff)