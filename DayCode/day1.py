def runCode():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    numbers = inputFile.readlines()

    currentDepth = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    dropCounter = 0
    line = 0
    max = len(numbers) - 2
    while line < max :
        int_depth = int(numbers[line]) + int(numbers[line + 1]) + int(numbers[line+ 2])
        if int_depth > currentDepth:
            dropCounter = dropCounter + 1
        currentDepth = int_depth
        line = line + 1
    print("Depth increases: " + str(dropCounter))