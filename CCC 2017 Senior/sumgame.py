n = int(input())
swift = input().split()
sema = input().split()

sumSwift = 0
sumSema = 0
equal = [0]

for s in range(n):
    sumSwift += int(swift[s])
    sumSema += int(sema[s])
    if sumSwift == sumSema:
        equal.append(s+1)
    
print(max(equal))