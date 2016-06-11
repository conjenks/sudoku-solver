class Cell:
    def __init__(self, value, isPermanent):
        self.value = 0
        self.isPermanent = False


def solve(board):  # solves the board
    if valid(board) is False:
        print("This board is unsolvable.")
        return
    row = 0  # begin in the first cell in the first row
    column = 0
    while row != 9:  # while there are still empty spaces in the 9 rows,
        if row <= 8 and column <= 8:
            row, column = add1(board, row, column)  # add 1 to the current cell
        if valid(board) is True and row != 9:  # if the board is valid,
            row, column = moveUp(row, column)
            continue  # restart
        if valid(board) is False:  # if the board is invalid,
            if board[row][column].value == 9:  # if the value of the current cell is equal to 9,
                board[row][column].value = 0  # set it equal to 0
                row, column = moveBack(board, row, column)
            continue  # restart


def add1(board, row, column):  # increments each cell
    while row <= 8 and column <= 8:
        if board[row][column].isPermanent and row != 8 and column != 8:
            row, column = moveUp(row, column)
            continue
        while board[row][column].value == 9 and board[row][column].isPermanent is False:  # if the value of the cell is equal to 9,
            board[row][column].value = 0  # set it equal to 0
            row, column = moveBack(board, row, column)
        if board[row][column].isPermanent is False:
            board[row][column].value += 1  # add 1 to the current cell
        return row, column  # return the new coordinate of the current cell

def moveUp(row, column):
    if column == 8:
        row += 1
        column = 0
    else:
        column += 1
    return row, column

def moveBack(board, row, column):
    while True:
        if column == 0:
            row -= 1
            column = 8
        else:
            column -= 1
        if board[row][column].isPermanent is False:
            return row, column


def valid(board):
    for i in range(1, 10):
        if checkRowsForDuplicate(board, i) is False:
            return False
        if checkColumnsForDuplicate(board, i) is False:
            return False
        if checkZonesForDuplicate(board, i) is False:
            return False
    return True


def checkRowsForDuplicate(board, x):
    for row in board:
        line = []
        for cell in row:
            line.append(cell.value)
        if line.count(x) > 1:
            return False


def checkColumnsForDuplicate(board, x):
    for i in range(0, 9):
        column = []
        for row in board:
            column.append(row[i].value)
        if column.count(x) > 1:
            return False


def checkZonesForDuplicate(board, x):
    y = [0, 3, 6]
    z = [3, 6, 9]
    for i in range(3):
        for j in range(3):
            if checkSingleZone(board, x, y[i], z[i], y[j], z[j]) is False:
                return False
    return True


def checkSingleZone(board, x, rowStart, rowEnd, columnStart, columnEnd):
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

def initializeBoard():
    board = [[], [], [], [], [], [], [], [], []]
    for row in board:
        for i in range(0, 9):
            row.append(Cell(0, False))
    return board