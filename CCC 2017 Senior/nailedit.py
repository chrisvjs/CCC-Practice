N = int(input())
boards = list(map(int, input().split()))


L = [0] * 2001
F = [0] * 4002
for b in boards:
    L[b] += 1

for i in range(0, len(L)- 1):
    for j in range(i, len(L)):
        if i == j:
            F[i+j] += L[i] // 2
        else:
            F[i+j] += min(L[i], L[j])

longest, size = 0 ,0

for fL in F:
    if fL > longest:
        longest = fL
        size = 1
    elif fL == longest:
        size +=1

print(longest, size)