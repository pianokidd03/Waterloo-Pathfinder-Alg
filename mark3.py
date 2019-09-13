textFile = open('map.txt', 'r')


factoryGrid = []

for columns in (raw.strip().split() for raw in textFile):
    inputGrid = []
    for i in range(0, len(columns[0])):
        inputGrid.append(str    (columns[0])[i])
    factoryGrid.append(inputGrid)


def seenByCam(row, col, grid):
    isSeenByCam = []

    startingPos = grid[row][col]

    # Up
    newRow = row
    while (startingPos != 'W') and (startingPos != 'C'):
        newRow = newRow-1
        startingPos = grid[newRow][col]

    if startingPos == 'W':
        isSeenByCam.append(False)
    elif startingPos == 'C':
            isSeenByCam.append(True)

    startingPos = grid[row][col]

    # Down
    newRow = row
    while (startingPos != 'W') and (startingPos != 'C'):
        newRow = newRow + 1
        startingPos = grid[newRow][col]

    if startingPos == 'W':
        isSeenByCam.append(False)
    elif startingPos == 'C':
            isSeenByCam.append(True)

    
    startingPos = grid[row][col]

    # Left
    newCol = col
    while (startingPos != 'W') and (startingPos != 'C'):
        newCol = newCol - 1
        startingPos = grid[row][newCol]

    if startingPos == 'W':
        isSeenByCam.append(False)
    elif startingPos == 'C':
            isSeenByCam.append(True)

    startingPos = grid[row][col]

    # Right
    newCol = col
    while (startingPos != 'W') and (startingPos != 'C'):
        newCol = newCol + 1
        startingPos = grid[row][newCol]

    if startingPos == 'W':
        isSeenByCam.append(False)
    elif startingPos == 'C':
            isSeenByCam.append(True)

    '''
    print(isSeenByCam[0])
    print(isSeenByCam[1])
    print(isSeenByCam[2])
    print(isSeenByCam[3])
    '''

    if (isSeenByCam[0] or isSeenByCam[1] or isSeenByCam[2] or isSeenByCam[3]) == False:
        return False
    else:
        return True


startRow = 0
startCol = 0

att = []


for i in range(0, len(factoryGrid)):
    attRow = []
    for a in range(0, len(factoryGrid[0])):
        if factoryGrid[i][a] == 'S':
            startRow = i
            startCol = a
            attRow.append(('S'))

        if factoryGrid[i][a] == 'W' or factoryGrid[i][a] == 'C':
            attRow.append('U')
        elif factoryGrid[i][a] == 'L' and (factoryGrid[i][a-1] == 'W' or factoryGrid[i][a-1] == 'C' or factoryGrid[i][a-1] == 'S'):
            attRow.append('U')
        elif factoryGrid[i][a] == 'R' and (factoryGrid[i][a+1] == 'W' or factoryGrid[i][a+1] == 'C' or factoryGrid[i][a+1] == 'S'):
            attRow.append('U')
        elif factoryGrid[i][a] == 'D' and (factoryGrid[i+1][a] == 'W' or factoryGrid[i+1][a] == 'C' or factoryGrid[i+1][a] == 'S'):
            attRow.append('U')
        elif factoryGrid[i][a] == 'U' and (factoryGrid[i-1][a] == 'W' or factoryGrid[i-1][a] == 'C' or factoryGrid[i-1][a] == 'S'):
            attRow.append('U')

        elif factoryGrid[i][a] == '.':

            if seenByCam(i, a, factoryGrid) == True:
                attRow.append('U')

            else:
                attRow.append('S')

        else:
            if factoryGrid[i][a] != 'S':
                attRow.append(('S'))
    att.append(attRow)


# Find route prgm...
for i in range(len(att)):
    print('Col'+str(i)+': '+str(att[i]))
print('startRow: '+str(startRow))
print('startCol: '+str(startCol))
print('Starring Pos is '+att[startRow][startCol])
print('\n')

def areSame(row, col, list):
    for i in range(len(list)):
        if (list[i][0] == row) and (list[i][1] == col):
            return True
    return False

def all_false(items):
    return all(x == False for x in items)

def all_col(list):
    all_cols = []
    for i in range(len(list)):
        all_cols.append(list[i][0])
    return all_cols

def all_row(list):
    all_rows = []
    for i in range(len(list)):
        all_rows.append(list[i][0])
    return all_rows

def surroundUnsafe(row, col, att):
    if (att[row+1][col] == 'U') and (att[row-1][col] == 'U') and (att[row][col+1] == 'U') and (att[row][col-1] == 'U'):
        return True
    else:
        return False

for r in range(len(att)):
    for c in range(len(att[r])):
        if att[r][c] == 'S' and factoryGrid[r][c] == '.' and surroundUnsafe(r, c, att) == True:
            print(-1)

        elif att[r][c] == 'S' and factoryGrid[r][c] == '.':
            # print('att: '+str(att[r][c]))
            endPointCol = c
            endPointRow = r

            pathList = []
            coord = []  # coordinates will ALWAYS be entered COL, ROW, NUMSTEPS

            coord.append(endPointRow)
            coord.append(endPointCol)
            coord.append(0)

            pathList.append(coord)

            # print('r: '+str(r))
            # print('c: '+ str(c))

            while areSame(startRow, startCol, pathList) == False:

                oldPathList = pathList

                for i in range(len(pathList)):

                    currentPos = pathList[i]

                    row = currentPos[0]
                    col = currentPos[1]
                    step = currentPos[2]

                    # print('col '+str(col))
                    # print('row'  + str(row))
                    # print('step ' + str(step))

                    # down:
                    areCoordSame = []
                    if att[row][col+1] == 'S':
                        coord = []
                        if areSame(row, col+1, pathList) == False:
                            coord.append(row)
                            coord.append(col+1)
                            coord.append(step + 1)
                            pathList.append(coord)

                    # up:
                    if att[row][col-1] == 'S':
                        coord = []
                        if areSame(row, col-1, pathList) == False:
                            coord.append(row)
                            coord.append(col-1)
                            coord.append(step + 1)
                            pathList.append(coord)

                    if att[row+1][col] == 'S':
                        coord = []
                        if areSame(row + 1, col, pathList) == False:
                            coord.append(row + 1)
                            coord.append(col)
                            coord.append(step + 1)
                            pathList.append(coord)
                        # print(pathList)

                    if att[row-1][col] == 'S':
                        coord = []
                        if areSame(row-1, col, pathList) ==  False:
                            coord.append(row-1)
                            coord.append(col)
                            coord.append(step+1)
                            pathList.append(coord)


            '''
            if pathList[-1][2] == 0:
                print('pathList: '+str(pathList))
                print('Row: ' + str(pathList[0][0]))
                print('Col: ' + str(pathList[0][1]))
                print(-1)
            else:
                print('pathList: '+str(pathList))
                print('Row: '+str(pathList[0][0]))
                print('Col: ' + str(pathList[0][1]))
                print('Steps: ' + str(pathList[-1][2]))
            '''

            def findActualPath(roughList):
                newPathList = []
                startRow = roughList[0][0]
                startCol = roughList[0][1]
                newPathList.append(roughList[0])
                for i in range(len(roughList)):
                    if i != 0:
                        totalDiff = abs(startRow - roughList[i][0]) + abs(startCol - roughList[i][1])
                        if totalDiff == 1:
                            newPathList.append(roughList[i])
                    startRow = newPathList[-1][0]
                    startCol = newPathList[-1][1]
                return newPathList

            newPathList = findActualPath(pathList)
            # print('\n' + 'newPathList: ' + str(newPathList))
            totalSteps = newPathList[-1][2]
            for i in range(len(newPathList)):
                if (factoryGrid[newPathList[i][0]][newPathList[i][1]] == 'U') or (factoryGrid[newPathList[i][0]][newPathList[i][1]] == 'D') or (factoryGrid[newPathList[i][0]][newPathList[i][1]] == 'L') or (factoryGrid[newPathList[i][0]][newPathList[i][1]] == 'R'):
                    totalSteps = totalSteps - 1
            print('adjusted total steps: '+ str(totalSteps))
        elif att[r][c] == 'U' and factoryGrid[r][c] == '.':
            print(-1)
