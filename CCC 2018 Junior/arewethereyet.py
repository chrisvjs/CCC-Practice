rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))

p = rints()

c = [0]
for i in range(0,4):
    c.append(c[i] + p[i])

for i in range(0,5):
    r = []
    for j in range(0,5):
        dist = abs(c[j] - c[i])
        r.append(dist)
    print(*r)
