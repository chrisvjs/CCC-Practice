rint = lambda: int(input())
rints = lambda: list(map(int,input().split()))

def prime(num):
	if num == 2:
		return True

	elif num == 1 or num == 0 or num%2 == 0:
		return False
	for count in range(3, int(num/2)+1, 2):
		if (num%count) == 0:
			return False
	return True

def generatePrimes(num):
    primeList = []
    for x in range(3, num):
        if prime(x):
            primeList.append(x)
    return primeList

test = rint()

numList = []

for _ in range(test):
    numList.append(rints())
    
for num in numList:
    for i in range(1, num):
        if i

