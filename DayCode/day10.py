def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day10Input.txt', 'r')]
    illegalTable = [0] * 4
    incompletes = []
    for line in inputs:
        #print()
        #print(line)
        stack = []
        hasIllegal = False
        for char in line:
            stackLength = len(stack)-1
            if char == ')':
                if(stack[stackLength] == "("):
                    #print("remove")
                    #stack.remove(stackLength)
                    stack.pop()
                else:
                    #print("Expected '" + stack[stackLength] + "', instead read '" + char + "'")
                    illegalTable[0] = illegalTable[0] + 1
                    hasIllegal = True
                    break
            elif char == ']':
                if(stack[stackLength] == "["):
                    #print("remove")
                    #stack.remove(stackLength)
                    stack.pop()
                else:
                    #print("Expected '" + stack[stackLength] + "', instead read '" + char + "'")
                    illegalTable[1] = illegalTable[1] + 1
                    hasIllegal = True
                    break
            elif char == '}':
                if(stack[stackLength] == "{"):
                    #print("remove")
                    #stack.remove(stackLength)
                    stack.pop()
                else:
                    #print("Expected '" + stack[stackLength] + "', instead read '" + char + "'")
                    illegalTable[2] = illegalTable[2] + 1
                    hasIllegal = True
                    break
            elif char == '>':
                if(stack[stackLength] == "<"):
                    #print("remove")
                    #stack.remove(stackLength)
                    stack.pop()
                else:
                    #print("Expected '" + stack[stackLength] + "', instead read '" + char + "'")
                    illegalTable[3] = illegalTable[3] + 1
                    hasIllegal = True
                    break
            else:
                stack.append(char)
            #if(len(stack) == 0):
                #print("all good")
        if(len(stack) > 0):
            if(not hasIllegal):
                incompletes.append(line)
    print(illegalTable)
    print("First Score: " + str((illegalTable[0] * 3) + (illegalTable[1] * 57) + (illegalTable[2] * 1197) + (illegalTable[3] * 25137)))
    print("############")
    print("incompletes: ")
    print("############")
    print(incompletes)

    listOfScores = []
    for line in incompletes:
        stack = []
        #print()
        #print(line)
        for char in line:
            stackLength = len(stack)-1
            if char == ')':
                if(stack[stackLength] == "("):
                    stack.pop()
            elif char == ']':
                if(stack[stackLength] == "["):
                    stack.pop()
            elif char == '}':
                if(stack[stackLength] == "{"):
                    stack.pop()
            elif char == '>':
                if(stack[stackLength] == "<"):
                    stack.pop()
            else:
                stack.append(char)
        stack.reverse()
        score = 0
        for char in stack:
            score = score * 5
            if(char == '('):
                score = score + 1
            elif(char == '['):
                score = score + 2
            elif(char == '{'):
                score = score + 3
            elif(char == '<'):
                score = score + 4
        #print("Score: " + str(score))
        listOfScores.append(score)
    listOfScores.sort()
    print("Middle: " + str(listOfScores[int(len(listOfScores)/2)]))