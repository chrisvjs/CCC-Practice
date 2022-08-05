n = int(input())
p = []
v = []
r = []
minL= []
maxL = []
t = []

for i in range(n):
    curr = input().split()
    p.append(int(curr[0]))
    v.append(int(curr[1]))
    r.append(int(curr[2]))
    minL.append((int(curr[0]) - int(curr[2])))
    maxL.append((int(curr[0]) + int(curr[2])))

maxNum = max(maxL)
minNum = min(minL)

for i in range(minNum, maxNum):
    b = 0
    for j in range(n):
        if abs(i - p[j]) <= r[j]:
            b+=0
        else:
            b += (abs(i - p[j]) - r[j]) * v[j]
    t.append(b)

if not t:
    print(0)
else:
    print(min(t))
