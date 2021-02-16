import math
n = int(input())
tides = list(map(int, input().split()))

highTides = []
lowTides = []

tides.sort()

r = 0
while r<n:
    if r < n/2:
        lowTides.append(tides[r])
    else:
        highTides.append(tides[r])
    r+=1

lowTides.sort(reverse=True)

for i in range(int(n//2)):
    print(lowTides[i], end = ' ')
    print(highTides[i], end = ' ')

q = math.ceil(n/2) -1
if n % 2 != 0:
    print(lowTides[q])