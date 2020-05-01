import graphics as g
from graphics import *

WN_MULT = 100

def getBoard(boardSize):
    # bSize = int(input("Board Size: "))
    bSize = boardSize * WN_MULT
    win = g.GraphWin("ChessBoard " + str(boardSize)+"x"+str(boardSize), bSize,bSize)
    return win

# Returns a dictionary with a key of column/row coordinate like "a1" and 
# Value needed to draw the corresponding rectangle
def genSquares(boardSize):
    sqDict  = {}
    #This loop applies chr and ord to generate a letter of a column
    for i in range(boardSize):
        colChar = chr(ord('a') + i)
        x = i * WN_MULT
        x2 = x + WN_MULT
        for j in range(boardSize):
            # create row nums
            rowNum = j + 1
            y = j * WN_MULT
            y2 = y + WN_MULT
            # print(colChar + str(rowNum) + "tlPoint: " + str(x) + " " + str(y) + " brPoint: " + str(x2) + " " + str(y2))
            sqId = colChar + str(rowNum)
            sqRect = g.Rectangle(Point(x,y),Point(x2,y2))
            sqDict[sqId] = sqRect
    return sqDict

def main():
    bSize = int(input("Board Size: "))
    bWin = getBoard(bSize)

    # Now I have a nice dictionary with all my squares
    squares = genSquares(bSize)
    for key in squares:
        # print(type(squares[key]))
        squares[key].draw(bWin)
    

    # Manually undraw, setfill, and redraw
    # TODO: make a method that does this for 'visited'
    print(squares['a1'])
    squares['a1'].undraw()
    squares['a1'].setFill('red')
    squares['a1'].draw(bWin)


    # Line experiment

    mL = Line(squares['a1'].getCenter(),squares['c8'].getCenter())
    mL.setFill('red')
    mL.draw(bWin)

    bWin.getMouse()
main()
