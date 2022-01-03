def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day6Input.txt', 'r')]
    fishList = calcFishInput(inputs)
    print(fishList)
    numDays = 256
    day = 1
    while day <= numDays:
        fishList = stepDay(fishList)
        day = day + 1
    print(fishList)
    sum = addUpFish(fishList)
    print("Sum: " + str(sum))

def addUpFish(fishList):
    sum = 0
    for fish in fishList:
        sum = sum + fish
    return sum

def stepDay(fishList):
    index = 0
    newFishList = [0] * 9
    while index < 9:
        numFish = fishList[index]
        if(index == 0):
            newFishList[8] = numFish
            newFishList[6] = newFishList[6] + numFish
        else:
            newFishList[index-1] = newFishList[index-1] + numFish
        index = index + 1
    return newFishList

def calcFishInput(inputs):
    fishList = [0] * 9
    fishes = inputs[0].split(",")
    for fish in fishes:
        if fish == "0":
            fishList[0] = fishList[0] + 1
        if fish == "1":
            fishList[1] = fishList[1] + 1
        if fish == "2":
            fishList[2] = fishList[2] + 1
        if fish == "3":
            fishList[3] = fishList[3] + 1
        if fish == "4":
            fishList[4] = fishList[4] + 1
        if fish == "5":
            fishList[5] = fishList[5] + 1
        if fish == "6":
            fishList[6] = fishList[6] + 1
        if fish == "7":
            fishList[7] = fishList[7] + 1           
        if fish == "8":
            fishList[8] = fishList[8] + 1
    return fishList