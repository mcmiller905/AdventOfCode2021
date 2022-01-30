def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day11Input.txt', 'r')]
    grid = makeGrid(inputs)
    maxX = len(grid[0])-1
    maxY = len(grid)-1
    printGrid(grid)
    needToGoAgain = False
    numFlashes = 0
    numSteps = 1000
    stepNum = 0
    numFlashed = 0
    count = 0
    flag = True
    #step loop
    #while stepNum < numSteps:
    while flag:
        # print()
        # print("####################")
        # print()
        # print("Step number: " + str(stepNum+1))
        grid = incAll(grid)
        numFlashed = numGotFlashed(grid)
        #print("flashed this round: " + str(numFlashed))
        needToGoAgain = (numFlashed > 0)
        numFlashes = numFlashes + numFlashed
        while(needToGoAgain):
            grid = flash(grid, maxX, maxY)
            numFlashed = numGotFlashed(grid)
            #print("flashed this round: " + str(numFlashed))
            needToGoAgain = (numFlashed > 0)
            numFlashes = numFlashes + numFlashed
        #print("NumFlashed: " + str(numFlashes))
        numStar = printGrid(grid)
        if(numStar == 100):
            flag = False
            print("step: " + str(stepNum+1))
        count = count + numStar
        stepNum = stepNum + 1
    print()
    #print("Num flashes: " + str(numFlashes))
    print("count: " + str(count))

def flash(grid, maxX, maxY):
    y = 0
    for row in grid:
        x = 0
        for num in row:
            if int(num) > 9:
                #start flash
                grid[y][x] = "0"
                #check upper
                if(y > 0):
                    #check left
                    if(x > 0):
                        if(grid[y-1][x-1] != "0"):
                            grid[y-1][x-1] = str(int(grid[y-1][x-1]) + 1)
                    #check center
                    if(grid[y-1][x] != "0"):
                        grid[y-1][x] = str(int(grid[y-1][x]) + 1)
                    #check right
                    if(x < maxX):
                        if(grid[y-1][x+1] != "0"):
                            grid[y-1][x+1] = str(int(grid[y-1][x+1]) + 1)
                #check same row
                #check left
                if(x > 0):
                        if(grid[y][x-1] != "0"):
                            grid[y][x-1] = str(int(grid[y][x-1]) + 1)
                #check right
                if(x < maxX):
                        if(grid[y][x+1] != "0"):
                            grid[y][x+1] = str(int(grid[y][x+1]) + 1)
                #check lower
                if(y < maxY):
                    #check left
                    if(x > 0):
                        if(grid[y+1][x-1] != "0"):
                            grid[y+1][x-1] = str(int(grid[y+1][x-1]) + 1)
                    #check center
                    if(grid[y+1][x] != "0"):
                        grid[y+1][x] = str(int(grid[y+1][x]) + 1)
                    #check right
                    if(x < maxX):
                        if(grid[y+1][x+1] != "0"):
                            grid[y+1][x+1] = str(int(grid[y+1][x+1]) + 1)
            x = x + 1
        y = y + 1
    return grid

def incAll(grid):
    newGrid = []
    for row in grid:
        newRow = []
        for num in row:
            newRow.append(str(int(num) + 1))
        newGrid.append(newRow)
    return newGrid

def numGotFlashed(grid):
    retval = 0
    for row in grid:
        for num in row:
            if int(num) > 9:
                retval = retval + 1
    return retval

def makeGrid(inputs):
    retval = []
    for line in inputs:
        row = []
        for num in line:
            row.append(num)
        retval.append(row)
    print(retval)
    return retval

def printGrid(grid):
    print()
    count = 0
    for row in grid:
        line = ""
        for num in row:
            if(num == "0"):
                num = "*"
                count = count + 1
            line = line + num
        print(line)
    return count