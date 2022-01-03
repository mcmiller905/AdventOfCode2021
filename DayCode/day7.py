def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day7Input.txt', 'r')]
    crabList = inputs[0].split(",")
    maximum = getMax(crabList)
    index = 0
    minimumDist = -1
    pointCon = -1
    while index <= maximum:
        distance = getTotalDistance(crabList, index)
        if(minimumDist == -1):
            minimumDist = distance
            pointCon = index
        elif(distance < minimumDist):
            minimumDist = distance
            pointCon = index
        index = index + 1
    print("Min Dist: " + str(minimumDist))
    print("Point of Contact: " + str(pointCon))

def getTotalDistance(crabList, index):
    totalDistance = 0
    for crab in crabList:
        distance = int(crab) - index
        if(distance < 0):
            distance = distance * -1
        fuel = (distance *(distance + 1)) / 2
        totalDistance = totalDistance + fuel
    return totalDistance

def getMax(crabList):
    max = 0
    for crab in crabList:
        if int(crab) > max:
            max = int(crab)
    return max