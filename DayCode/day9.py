def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day9Input.txt', 'r')]
    lowList = getListOfLowPoints(inputs)
    listOfSizes = []
    maxX = len(inputs[0])-1
    # print("Max X: " + str(maxX))
    maxY = len(inputs)-1
    # print("Max Y: " + str(maxY))
    # print("Low Points: ")
    # print(lowList)
    for lowPoint in lowList:
        # print("#####")
        # print("x: " + str(lowPoint[0]) + " | y: " + str(lowPoint[1]))
        # print("#####")
        pointsToCheck = [lowPoint]
        pointsInGroup = [lowPoint]
        while True:
            pointsThisRound = []
            for point in pointsToCheck:
                # print("Checking: " + str(point))
                pointsThisRound = addAllMissing(pointsThisRound, pointsInGroup, getAdj(point, inputs, maxX, maxY))
                pointsInGroup = addAllMissing(pointsInGroup, pointsInGroup, pointsThisRound)
                pointsToCheck = pointsThisRound
            if(len(pointsToCheck) == 0):
                break
        # print(pointsInGroup)
        listOfSizes.append(len(pointsInGroup))
    # print(listOfSizes)
    listOfSizes.sort(reverse=True)
    print(listOfSizes)
    print("Answer: " + str(listOfSizes[0] * listOfSizes[1] * listOfSizes[2]))

def getAdj(point, inputs, maxX, maxY):
    # print("in adj point: " + str(point))
    # print("point[0]: " + str(point[0]))
    # print("point[1]: " + str(point[1]))
    adjPoints = []
    x = point[0]
    y = point[1]
    #check left direction
    if(x > 0):
        if(int(inputs[y][x-1]) < 9):
            #adjPoints.append((y, (x-1)))
            adjPoints.append(((x-1), y))
    #check right direction
    if(x < maxX):
        # print("x: " + str(x) + " | maxX: " + str(maxX))
        # print("y: " + str(y) + " | maxY: " + str(maxY))
        if(int(inputs[y][x+1]) < 9):
            #adjPoints.append((y, x+1))
            adjPoints.append((x+1, y))
    #check up direction
    if(y > 0):
        if(int(inputs[y-1][x]) < 9):
            #adjPoints.append((y-1, x))
            adjPoints.append((x, y-1))
    #check down direction
    if(y < maxY):
        if(int(inputs[y+1][x]) < 9):
            #adjPoints.append((y+1, x))
            adjPoints.append((x, y+1))
    return adjPoints

def getListOfLowPoints(inputs):
    rowIndex = 0
    lowPoints = []
    while rowIndex < len(inputs):
        colIndex = 0
        line = inputs[rowIndex]
        while colIndex < len(line):
            isLowPoint = True
            currentHeight = int(inputs[rowIndex][colIndex])
            #check above
            if(rowIndex > 0):
                if currentHeight >= int(inputs[rowIndex-1][colIndex]):
                    isLowPoint = False
            #check below
            if(rowIndex < (len(inputs)-1)):
                if currentHeight >= int(inputs[rowIndex+1][colIndex]):
                    isLowPoint = False
            #check left
            if(colIndex > 0):
                if currentHeight >= int(inputs[rowIndex][colIndex-1]):
                    isLowPoint = False
            #check right
            if(colIndex < (len(line)-1)):
                if currentHeight >= int(inputs[rowIndex][colIndex+1]):
                    isLowPoint = False
            if(isLowPoint):
                coord = (colIndex, rowIndex)
                lowPoints.append(coord)
            colIndex = colIndex + 1
        #print(line)
        rowIndex = rowIndex + 1
    #print("Risk Level:")
    #print(str(sumUp(lowPoints) + len(lowPoints)))
    return lowPoints

#only used for part 1
def sumUp(lowPoints):
    retval = 0
    for point in lowPoints:
        retval = retval + int(point)
    return retval

def addAllMissing(listToAddTo, itemsInGroup,listOfItems):
    for item in listOfItems:
        addIt = True
        for groupItem in itemsInGroup:
            if(item == groupItem):
                addIt = False
                break
        if(addIt):
            listToAddTo.append(item)
    return listToAddTo