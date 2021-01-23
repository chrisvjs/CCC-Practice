
paintDrops = int(input())
xCoordList = []
yCoordList = []

for x in range(paintDrops):
    xCoord, yCoord = input().split(',')
    xCoordList.append(int(xCoord))
    yCoordList.append(int(yCoord))

xSmall = min(xCoordList) -1
ySmall = min(yCoordList) -1
xBig = max(xCoordList) + 1
yBig = max(yCoordList) + 1

print("{0},{1}".format(xSmall, ySmall))
print("{0},{1}".format(xBig, yBig))