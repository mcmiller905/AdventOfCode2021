def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day8Input.txt', 'r')]
    counter = 0
    for line in inputs:
        output = ""
        lineSplit = line.split(" | ")
        feed = lineSplit[0]
        feedNums = feed.split(" ")
        exampleNumArray = readFeed(feedNums)
        display = lineSplit[1]
        displayNums = display.split(" ")
        for num in displayNums:
            if(len(num) == 2):
                output = output + "1"
            elif(len(num) == 3):
                output = output + "7"
            elif(len(num) == 4):
                output = output + "4"
            elif(len(num) == 7):
                output = output + "8"
            elif(len(num) == 5):
                if containsNumComponents(num, exampleNumArray[1]):
                    output = output + "3"
                elif containsAtLeast3NumComponents(num, exampleNumArray[4]):
                    output = output + "5"
                else:
                    output = output + "2"
            elif(len(num) == 6):
                if containsNumComponents(num, exampleNumArray[4]):
                    output = output + "9"
                elif doesntContainNumComponents(num, exampleNumArray[7]):
                    output = output + "6"
                else:
                    output = output + "0"
            else:
                output = output + "#"
        print(output)
        counter = counter + int(output)
    print("sum: " + str(counter))

def readFeed(feedNums):
    retval = [""] * 9
    for feedNum in feedNums:
        if(len(feedNum) == 2):
            retval[1] = feedNum
        elif(len(feedNum) == 3):
            retval[7] = feedNum
        elif(len(feedNum) == 4):
            retval[4] = feedNum
        elif(len(feedNum) == 7):
            retval[8] = feedNum
    return retval

def containsNumComponents(num, exampleNum):
    overallFlag = True
    for exampleLetter in exampleNum:
        letterFlag = False
        for numLetter in num:
            if(numLetter == exampleLetter):
                letterFlag = True
        if(not letterFlag):
            overallFlag = False
    return overallFlag

def containsAtLeast3NumComponents(num, exampleNum):
    numContained = 0
    for exampleLetter in exampleNum:
        letterFlag = False
        for numLetter in num:
            if(numLetter == exampleLetter):
                letterFlag = True
                numContained = numContained + 1
        if(not letterFlag):
            overallFlag = False
    return (numContained >= 3)

def doesntContainNumComponents(num, exampleNum):
    overallFlag = True
    for exampleLetter in exampleNum:
        letterFlag = False
        for numLetter in num:
            if(numLetter == exampleLetter):
                letterFlag = True
        if(not letterFlag):
            overallFlag = False
    return not overallFlag