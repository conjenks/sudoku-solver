def check_single_zone(a, b, c, d, x): # a, b, c, and d represent the
    zone = []
    for row in board[a:b]:
        for column in row[c:d]:
            zone.append(column)
    if zone.count(x) > 1:
        return False

def check_zones(x):
    y = [0, 3, 6]
    z = [3, 6, 9]
    for i in range(3):
        for j in range(3):
            if check_single_zone(y[i], z[i], y[j], z[j], x) == False:
                return False
    return True

def check_columns(x):
    for i in range(0,9):
        column = []
        for row in board:
            column.append(row[i])
        if column.count(x) > 1:
            return False

def check_rows(x):
    for row in board:
        if row.count(x) > 1:
            return False

def check_board():
    for i in range(1,10):
        if check_rows(i) == False:
            return False
        if check_columns(i) == False:
            return False
        if check_zones(i) == False:
            return False
    return True

def init_board():
    board = [[],[],[],[],[],[],[],[],[]]
    for i in board:
        for x in range(0,9):
            i.append(0)
    return board

board = init_board()

def add1(row, column):          #increments each cell
    if board[row][column] == 9:     #if the value of the cell is equal to 9,
        board[row][column] = 0          #set it equal to 0
        if column == 0:                 #if in the first cell of a row,
            row -= 1                        #go back a row, to the last cell
            column = 8
        else:                           #if not in the first cell,
            column -= 1                     #go to the previous cell
    board[row][column] += 1         #add 1 to the current cell
    return row, column              #return the new coordinate of the current cell

def solve():                        #solves the board
    row = 0                                 #begin in the first cell in the first row
    column = 0
    while row != 9:                         #while there are still empty spaces in the 8 rows,
        row, column = add1(row, column)         #add 1 to the current cell
        for line in board:                      #print the board
            print(line)
        print(), print()
        if check_board() == True:               #if the board is valid,
            if column == 8:                         #if in the last cell of a row,
                row += 1                                #move up one row, and begin in the first cell
                column = 0
            else:                                   #otherwise, move on to the next cell
                column += 1
            continue                                #restart
        if check_board() == False:              #if the board is invalid,
            if board[row][column] == 9:             #if the value of the current cell is equal to 9,
                board[row][column] = 0                  #set it equal to 0
                if column == 0:                         #if in the first cell of a row,
                    row -= 1                                #go back a row, and into the last cell
                    column = 8
                else:                                   #otherwise, move back to the previous cell
                    column -= 1
            continue                                #restart



solve()





