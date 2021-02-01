
rint = lambda: int(input())
rints = lambda: list(map(int, input().split()))

test = rint()

numList = []

for _ in range(test):
    numList.append(rint())


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for n in numList:
    for i in range(2, n*2):
        if isPrime(i) == True and isPrime((n*2)-i) == True:
            print(str(i) + " " + str((n*2)-i))
            break
                

