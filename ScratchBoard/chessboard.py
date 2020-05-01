import graphics as g
from graphics import *

WN_MULT = 100

# window = g.GraphWin("ChessBoard",800,800)
a1 = g.Rectangle(Point(0,0), Point(100,100))
a2 = g.Rectangle(Point(0,100),Point(100,200))
a3 = g.Rectangle(Point(0,200),Point(100,300))


squares = []
squares.append(a1)
squares.append(a2)
squares.append(a3)

def getBoard():
    bSize = int(input("Board Size: "))
    bSize = bSize * WN_MULT
    win = g.GraphWin("ChessBoard " + str(bSize), bSize,bSize)
    return win

def genSquares(boardSize):
    

def genBoard(window,squaresList):
    i=0
    for square in squaresList:
        i = i+1
        square.setOutline('black')
        if i % 2:
            square.setFill('black')
        square.draw(window)



def main():
    bWin = getBoard()

    genBoard(bWin, squares)

    bWin.getMouse()
main()
