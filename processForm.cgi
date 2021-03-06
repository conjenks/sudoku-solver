#!C:\Python34\python.exe

import cgi
import cgitb
from sudokuSolver import *

def htmlTop():
    print("""Content-type:text/html\n\n
        <!DOCTYPE html>
        <html>
        <title>Sudoku Solver</title>
        <head><link href="style.css" rel="stylesheet" type="text/css"></head>
        <body>
        <h1 align=center>Sudoku Solver</h1>""")

def htmlBody(board):
    print("<table align=center>")
    for i in range(9):
        print("<tr>")
        for j in range(9):
            if board[i][j].isPermanent:
                print("""<td align="center" bgcolor="aqua">%s</td>""" % board[i][j].value)
            else:
                print("""<td align="center">%s</td>""" % board[i][j].value)
        print("</tr>")
    print("</table>")

def htmlTail():
    print("</body></html>")

def populate(board):
    formData = cgi.FieldStorage()
    for i in range(9):
        for j in range(9):
            dataCoordinates = (i, j)
            dataCoordinates = "%s%s" % dataCoordinates
            if dataCoordinates in formData:
                value = formData.getvalue(dataCoordinates)
                board[i][j].value = int(value)
                board[i][j].isPermanent = True

if __name__ == "__main__":
    cgitb.enable()
    try:
        htmlTop()
        board = initializeBoard()
        populate(board)
        if valid(board) is False:
            print("<p align=center>That board is unsolvable. Please enter appropriate values.</p>")
        else:
            solve(board)
            htmlBody(board)
        htmlTail()
    except:
        cgi.print_exception()



