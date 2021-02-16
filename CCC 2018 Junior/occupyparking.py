n = int(input())
rstrs = lambda: input()

dayOne = []
dayTwo = []

p = rstrs()
l = rstrs()

for char in p:
    dayOne.append(char)

for char in l:
    dayTwo.append(char)

c =0

for r in range(len(dayOne)):
    if dayOne[r] == 'C' and dayTwo[r] == 'C':
        c += 1

print(c)