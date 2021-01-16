
userInt = lambda: int(input())
userInts = lambda: list(map(int, input().split()))

r, c = userInt(), userInt()

grid = []
for _ in range(r):
    grid.append(userInts())

factors = {}




