intin = lambda: int(input())
intsin = lambda: list(map(int, input().split()))
stringin = lambda: input()
stringsin = lambda: input().split()


j, a = intin(), intin()

jL = []

aL = []

for _ in range(j):
    jL.append(stringin())

for _ in range(a):
    aL.append(stringsin())

sC = {}
mC = {}
lC = {}
count = 0
sellCount = 0


for x in jL:
    count += 1
    if x == 'S':
        sC[count] = 'S'
    elif x == 'M':
        mC[count] = 'M'
    elif x == 'L':
        lC[count] = 'L'





