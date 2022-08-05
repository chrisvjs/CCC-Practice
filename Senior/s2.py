m, n, k = int(input()), int(input()), int(input())
type = []
curr = []
grid = []*m
for x in range(n):
    grid.append([0]* n)
c= 0
for i in range(k):
    type.append(input().split())
for i in type:
    if type.count(i) % 2 != 0 and i not in curr:
        curr.append(i)
for i in range(len(curr)):
    num = int(curr[i][1])
    if curr[i][0] == "R":
        for j in range(n):
            if grid[num-1][j] == 0:
                grid[num-1][j] = 1
                c+=1
            else:
                grid[num-1][j] = 0
                c-=1
    else:
        for j in range(m):
            if grid[j][num-1] == 0:
                grid[j][num-1] = 1
                c+=1
            else:
                grid[j][num-1] = 0
                c-=1
print(c)
