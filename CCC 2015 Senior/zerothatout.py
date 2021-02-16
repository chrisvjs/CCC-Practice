intin = lambda: int(input())
intsin = lambda: list(map(int, input().split()))

n = intin()

stack = []
ans = 0
for x in range(n):
    num = intin()

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for x in stack:
    ans += x

print(ans)
