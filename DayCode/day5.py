def runCode():
    inputs = [line.rstrip() for line in open('InputFiles/day5Input.txt', 'r')]
    grid = [[0 for col in range(1000)] for row in range(1000)]

    for line in inputs:
        firstPoint = line.split(" -> ")[0]
        secondPoint = line.split(" -> ")[1]
        x1 = int(firstPoint.split(",")[0])
        y1 = int(firstPoint.split(",")[1])
        x2 = int(secondPoint.split(",")[0])
        y2 = int(secondPoint.split(",")[1])
        #print("x1: " + x1 + " y1: " + y1 + " x2: " + x2 + " y2: " + y2)
        if(x1 == x2):
            #print("got hori")
            #print("x1: " + str(x1) + " y1: " + str(y1) + " x2: " + str(x2) + " y2: " + str(y2))
            if(y1 < y2):
                start = y1
                end = y2
            else:
                start = y2
                end = y1
            index = start
            while index <= end:
                index = index + 1
                grid[index-1][x1] = grid[index-1][x1] + 1
        elif(y1 == y2):
            #print("got vert")
            #print("x1: " + str(x1) + " y1: " + str(y1) + " x2: " + str(x2) + " y2: " + str(y2))
            if(x1 < x2):
                start = x1
                end = x2
            else:
                start = x2
                end = x1
            index = start
            while index <= end:
                index = index + 1
                grid[y1][index-1] = grid[y1][index-1] + 1
        elif((x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1)):
            #print("got pos diag")
            #print("x1: " + str(x1) + " y1: " + str(y1) + " x2: " + str(x2) + " y2: " + str(y2))
            if(x1 < x2):
                startx = x1
                endx = x2
            else:
                startx = x2
                endx = x1
            if(y1 < y2):
                starty = y1
                endy = y2
            else:
                starty = y2
                endy = y1
            indexx = startx
            indexy = starty
            while indexx <= endx:
                indexx = indexx + 1
                indexy = indexy + 1
                grid[indexy-1][indexx-1] = grid[indexy-1][indexx-1] + 1
        else:
            print("got neg diag")
            print("x1: " + str(x1) + " y1: " + str(y1) + " x2: " + str(x2) + " y2: " + str(y2))
            if(x1 <= x2):
                startx = x1
                endx = x2
            else:
                startx = x2
                endx = x1
            if(y1 > y2):
                starty = y1
                endy = y2
            else:
                starty = y2
                endy = y1
            indexx = startx
            indexy = starty
            while indexx <= endx:
                indexx = indexx + 1
                indexy = indexy - 1
                grid[indexy+1][indexx-1] = grid[indexy+1][indexx-1] + 1
    printGrid(grid)
    pointsGT2(grid)

def printGrid(grid):
    for row in grid:
        rowString = ""
        for space in row:
            if(space == 0):
                rowString = rowString +  ". "
            else:
                rowString = rowString + str(space) + " "
        print(rowString)

def pointsGT2(grid):
    numPoints = 0
    for row in grid:
        for space in row:
            if(int(space) >= 2):
                numPoints = numPoints + 1
    print("num: " + str(numPoints))

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2