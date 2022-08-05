N = int(input())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
ans = 0
for i in range(N):
    tA = ((max(h[i], h[i+1]) - min(h[i], h[i+1])) * w[i]) /2
    rA = min(h[i],h[i+1]) * w[i]
    ans += (tA + rA)
print(ans)