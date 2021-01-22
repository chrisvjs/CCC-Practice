obs = lambda: int(input())
times = lambda: list(map(int, input().split()))

n = obs()
pairs = []
    
for _ in range(n):
    pairs.append(times())

pairs.sort()

ans = max(abs((pairs[i][1] - pairs[i-1][1]) / (pairs[i][0] - pairs[i-1][0]))for i in range(n))

print(ans)

