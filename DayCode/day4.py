def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day4Input.txt', 'r')]

    draws = inputs[0].split(",")
    boards = getBoards(inputs[1:])
    numBoards = len(boards)
    print(numBoards)
    newBoards = []
    winningBoard = []
    won = False
    finalWon = False
    finalCall = -1
    # print("## list the boards ##")
    # print(boards)
    # print("#####################")
    #for each number pulled
    newBoards.clear
    for num in draws:
        for board in boards:
            updatedBoard = markBoard(num, board)
            won = checkBoard(updatedBoard)
            if(won):
                print(num)
                won = False
                if(len(boards) == 1):
                    finalWon = True
                    winningBoard = updatedBoard
                    printBoard(winningBoard)
                    finalCall = num
                    break
            else:
                newBoards.append(updatedBoard)
        boards = newBoards
        newBoards = []
        if(finalWon):
            break
    #if won, calc answer
    if(finalWon):
        calcAnswer(winningBoard, finalCall)
    # print("## updated boards ##")
    # print(boards)
    # print("####################")

def getBoards(inputs):
    retval = []
    board = []
    for line in inputs:
        if(line != ""):
            numList = line.split(" ")
            for num in numList:
                if(num != ""):
                    board.append(num)
        else:
            if(board != []):
                retval.append(board)
            board = []
    if(board != []):
            retval.append(board)
    return retval

def markBoard(num, board):
    updatedBoard = []
    for space in board:
        if(space == num):
            updatedBoard.append(str(int(space) + 100))
        else:
            updatedBoard.append(space)
    return updatedBoard

def checkBoard(board):
    retval = False
            #check horizontals
    if (checkGroup(board, [0,1,2,3,4]) or 
            checkGroup(board, [5,6,7,8,9]) or
            checkGroup(board, [10,11,12,13,14]) or
            checkGroup(board, [15,16,17,18,19]) or
            checkGroup(board, [20,21,22,23,24]) or
            #check verticals
            checkGroup(board, [0,5,10,15,20]) or
            checkGroup(board, [1,6,11,16,21]) or
            checkGroup(board, [2,7,12,17,22]) or
            checkGroup(board, [3,8,13,18,23]) or
            checkGroup(board, [4,9,14,19,24])):
        retval = True
        print("got one")
    return retval

def checkGroup(board, spaces):
    retval = True
    for space in spaces:
        if(int(board[space]) < 100):
            retval = False
    return retval

def calcAnswer(board, numCalled):
    sum = 0
    for space in board:
        if(int(space) < 100):
            sum = sum + int(space)
    print("sum: " + str(sum))
    print("numCalled: " + str(numCalled))
    answer = sum * int(numCalled)
    print("Answer: " + str(answer))

def printBoard(board):
    print()
    print(board[0:5])
    print(board[5:10])
    print(board[10:15])
    print(board[15:20])
    print(board[20:25])
    print()