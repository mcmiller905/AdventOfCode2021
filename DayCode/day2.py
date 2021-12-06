def runCode():
    inputFile = open('InputFiles/day2Input.txt', 'r')
    inputs = inputFile.readlines()

    x = 0
    y = 0
    aim = 0
    for line in inputs:
        spaceIndex = line.index(' ')
        direction = line[0:spaceIndex]
        amount = int(line[spaceIndex+1:])
        if direction == "forward":
            x = x + amount
            y = y + (amount * aim)
        if direction == "up":
            aim = aim - amount
        if direction == "down":
            aim = aim + amount
    answer = x * y
    print("answer: " + str(answer))