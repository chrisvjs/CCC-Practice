from collections import defaultdict


intin = lambda: int(input())
intsin = lambda: list(map(int, input().split()))


m, n = intin(), intin()

grid = []

for _ in range(m):
    grid.append(intsin())

factors = defaultdict(list)

def fact(num):
    i = 1
    while i*i <= num:
        if num % i == 0 and i <= max(m,n) and num // i <= max(m,n):
            factors[num].append(i)
        i += 1
    return num

def solve(i,j):
    if i == m-1 and j == n-1:
        return True
    
    if i>= m or j >= n or grid[i][j] in factors:
        return False
        
    p = fact(grid[i][j])
    for q in factors[p]:
        r = p // q

        if solve(q-1 ,r-1) or solve(r-1, q-1):
            return True
    return False


if solve(0,0):
    print('yes')
else:
    print('no')
