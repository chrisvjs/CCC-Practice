m, n, k = int(input()), int(input()), int(input())
type = []
grid = [] *m
for x in range(n):
    grid.append([0]* n)
c= 0
f = {}
tC = []
tR = []
for i in range(k):
    s = input()
    type.append(s)

    if s in f.keys():
        f[s] = f.get(s)+1
    else:
        f[s] = 1

for i in range(k):
    try:
        if(f.get(type[i]) % 2 != 0):
            curr = type[i].split()
            num = int(curr[1])

            if curr[0] == "R":
                c += n-2 * len(tC)
                tR.append(curr[1])
            elif curr[0] == "C":
                c += m-2 * len(tR)
                tC.append(curr[1])
        
            del f[type[i]]
    except:
        continue
print(c)

    
