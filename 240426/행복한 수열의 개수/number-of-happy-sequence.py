n, m = map(int, input().split())

seqs = [list(map(int, input().split())) for _ in range(n)]

answer = 0 

for col in range(n):
    cols = []
    for row in range(n):
        cols.append(seqs[row][col])
    seqs.append(cols)

for seq in seqs:
    count = 1
    for i in range(n-m+1):
        if seq[i:i+m].count(seq[i]) == m:
            answer+=1
            break

print(answer)