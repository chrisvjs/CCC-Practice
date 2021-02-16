t = int(input())

for _ in range(t):
    n = int(input())
    lake = []
    p = [0] 
    c = [0]

    for j in range(n):
        c.append(int(input()))

    j = 1
    success = True

    while True:
        if c[len(c)-1] == j:
            lake.append(c[len(c)-1])
            c.remove(c[len(c)-1])
            j+=1
        elif p[len(p)-1] == j:
            lake.append(p[len(p)-1])
            p.remove(p[len(p)-1])
            j+=1
        elif len(c) > 1:
            p.append(c[len(c)-1])
            c.remove(c[len(c)-1])
        else:
            success = False
            break
        if j-1 == n:
            break
    if success == False:
        print("N")
    else:
        print("Y")