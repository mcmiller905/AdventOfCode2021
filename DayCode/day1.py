def runCode():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    numbers = inputFile.readlines()

    currentDepth = int(numbers[0])
    dropCounter = 0
    for depth in numbers :
        int_depth = int(depth)
        if int_depth > currentDepth:
            dropCounter = dropCounter + 1
        currentDepth = int_depth
    print("Depth increases: " + str(dropCounter))