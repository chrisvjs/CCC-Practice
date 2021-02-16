numList = []

for _ in range(4):
    numList.append(input())

firstTrue = False
midTrue = False
lastTrue = False


if numList[0] == '8' or numList[0] == '9':
    firstTrue = True

if numList[3] == '8' or numList[3] == '9':
    lastTrue = True

if numList[1] == numList[2]:
    midTrue = True

if midTrue and lastTrue and firstTrue:
    print("ignore")
else:
    print("answer")
