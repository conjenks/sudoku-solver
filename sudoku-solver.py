class Cell:
    def __init__(self, value, isPermanent):
        self.value = 0
        self.isPermanent = False


class Zones:
    def __init__(self, rowStart, rowEnd, columnStart, columnEnd):
        self.rowStart = rowStart
        self.rowEnd = rowEnd
        self.columnStart = columnStart
        self.columnEnd = columnEnd


def solve(board):  # solves the board
    row = 0  # begin in the first cell in the first row
    column = 0
    while row != 9:  # while there are still empty spaces in the 9 rows,
        row, column = add1(row, column)  # add 1 to the current cell
        printBoard(board)
        print(), print()
        if isValid(board) is True:  # if the board is valid,
            if column == 8:  # if in the last cell of a row,
                row += 1  # move up one row, and begin in the first cell
                column = 0
            else:  # otherwise, move on to the next cell
                column += 1
            continue  # restart
        if not isValid(board):  # if the board is invalid,
            if board[row][column].value == 9:  # if the value of the current cell is equal to 9,
                board[row][column].value = 0  # set it equal to 0
                if column == 0:  # if in the first cell of a row,
                    row -= 1  # go back a row, and into the last cell
                    column = 8
                else:  # otherwise, move back to the previous cell
                    column -= 1
            continue  # restart


def initializeBoard():
    board = [[], [], [], [], [], [], [], [], []]
    for row in board:
        for i in range(0, 9):
            row.append(Cell(0, False))
    return board


def add1(row, column):  # increments each cell
    if board[row][column].value == 9:  # if the value of the cell is equal to 9,
        board[row][column].value = 0  # set it equal to 0
        if column == 0:  # if in the first cell of a row,
            row -= 1  # go back a row, to the last cell
            column = 8
        else:  # if not in the first cell,
            column -= 1  # go to the previous cell
    board[row][column].value += 1  # add 1 to the current cell
    return row, column  # return the new coordinate of the current cell


def isValid(board):
    for i in range(1, 10):
        if checkRowsForDuplicate(i) is False:
            return False
        if checkColumnsForDuplicate(i) is False:
            return False
        if checkZonesForDuplicate(i) is False:
            return False
    return True


def checkRowsForDuplicate(x):
    for row in board:
        line = []
        for cell in row:
            line.append(cell.value)
        if line.count(x) > 1:
            return False


def checkColumnsForDuplicate(x):
    for i in range(0, 9):
        column = []
        for row in board:
            column.append(row[i].value)
        if column.count(x) > 1:
            return False


def checkZonesForDuplicate(x):
    y = [0, 3, 6]
    z = [3, 6, 9]
    for i in range(3):
        for j in range(3):
            if checkSingleZone(x, y[i], z[i], y[j], z[j]) is False:
                return False
    return True


def checkSingleZone(x, rowStart, rowEnd, columnStart, columnEnd):
    zoneValues = []
    for row in board[rowStart:rowEnd]:
        for column in row[columnStart:columnEnd]:
            zoneValues.append(column.value)
    if zoneValues.count(x) > 1:
        return False


def printBoard(board):
    for row in board:
        line = []
        for cell in row:
            line.append(cell.value)
        print(line)


board = initializeBoard()
solve(board)


# TO check the zones, we will check each of the 9 zones
# TO check one of the 9 zones, we will check the values within its coordinates
