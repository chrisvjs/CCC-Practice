rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))

n = rint()

s = []
for _ in range(n):
    s.append(rints())

min = s[0][0]
row = 0
col = 0

if s[0][n-1] < min:
    row = 0
    col = n-1
    min = s[0][n-1]
if s[n-1][0]  < min:
    row = n - 1
    col = 0
    min - s[n-1][0]
if s[n-1][n-1] < min:
    row = n-1
    col = n-1
    min = s[n-1][n-1]


if row == 0 and col == 0:
    for i in range(n):
        for j in range(n):
            print(s[i][j], end=" ")
        print()
elif row == 0 and col > 0:
    for i in range(n-1, -1 ,-1):
        for j in range(n):
            print(s[j][i], end=" ")
        print()
elif row > 0 and col > 0:
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            print(s[i][j], end=" ")
        print()
else:
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(s[j][i], end=" ")
        print()