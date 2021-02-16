vil = int(input())

disList = []
for _ in range(vil):
    disList.append(int(input()))

disList.sort()

ans = 2e9

for i in range(1,len(disList)):
    if i < len(disList)-1:
        ans = min(ans, ((disList[i] - disList[i-1]) / 2) + ((disList[i+1] - disList[i]) /2))

print(ans)