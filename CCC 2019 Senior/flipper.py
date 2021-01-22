strs = lambda: input()
wmat = lambda mat, sep: '\n'.join(sep.join(map(str, row)) for row in mat)

grid = [
    [[[1,2],[3,4]], [[2,1],[4,3]]],
    [[[3,4],[1,2]], [[4,3],[2,1]]]
]


str1 = strs()
h= v= 0
for char in str1:
    if char == 'H':
        h = 1 - h
    else:
        v = 1 - v

print(wmat(grid[h][v], ' '))

