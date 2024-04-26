n, m = map(int, input().split())

seqs = [list(map(int, input().split())) for _ in range(n)]

num_happy = 0

for col in range(n):
    cols = []
    for row in range(n):
        cols.append(seqs[row][col])
    seqs.append(cols)

for seq in seqs:
    count = 1
    for i in range(n-1):
        if seq[i] == seq[i+1]:
            count += 1
        else:
            count = 1
    
    if count >= m:
        num_happy += 1

print(num_happy)