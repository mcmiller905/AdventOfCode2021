def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day3Input.txt', 'r')]
    idk(inputs)
    
def getDigit(position, getMost, getOxy, lines):
    num0 = 0
    num1 = 0
    for line in lines:
        if(line[position] == "1"):
            num1 = num1 + 1
        else:
            num0 = num0 + 1
    retval = 0
    #print("Number of 0s: " + str(num0) + " Number of 1s: " + str(num1))
    if num0 == num1:
        if getOxy:
            retval = 1
        else:
            retval = 0
    elif num0 > num1:
        if getMost:
            retval = 0
        else:
            retval = 1
    else:
        if getMost:
            retval = 1
        else:
            retval = 0
    #print("retval: " + str(retval))
    return retval

def idk(inputs):
    print("=================")
    print("== Second Part ==")
    pos = 0
    length = len(inputs[0])
    lines = inputs
    newLines = []
    while pos < length:
        bit = getDigit(pos, True, True, lines)
        #print("pos: " + str(pos) + " bit: " + str(bit))
        for line in lines:
            if int(line[pos]) == bit:
                newLines.append(line)
                #print("Position: " + str(pos) + " : Bit: " + str(bit) + "   |  " + str(line))
        pos = pos + 1
        lines = newLines
        newLines = []
        #print("size: " + str(len(lines)))
        if(len(lines) == 1):
            break
    mostP2 = lines[0]

    pos = 0
    lines = inputs
    newLines = []
    while pos < length:
        bit = getDigit(pos, False, False, lines)
        #print("bit: " + str(bit))
        for line in lines:
            if int(line[pos]) == bit:
                newLines.append(line)
                #print(str(line))
        pos = pos + 1
        lines = newLines
        newLines = []
        if(len(lines) == 1):
            break
    leastP2 = lines[0]

    decMostP2 = int(mostP2,2)
    decLeastP2 = int(leastP2,2)
    print("Most: " + mostP2)
    print("Most Dec: " + str(decMostP2))
    print("Least: " + leastP2)
    print("Least Dec: " + str(decLeastP2))
    print("mult: " + str(decMostP2 * decLeastP2))