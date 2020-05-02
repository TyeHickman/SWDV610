import graphics as g
from graphics import *
import Graph as gr
from Graph import *
import graphedKnightsTour as gkt
import time

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
        # create column chars
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
    # bSize = int(input("Board Size: "))
    bSize = 8
    searchLimit = (bSize*bSize) - 1
    bWin = getBoard(bSize)
    #Get graph of all legal moves
    knightsGraph = gkt.knightGraph(bSize)
    # for em in knightsGraph:
    #     print(em.getId())


    # initialize this for the tour
    knightsPath = []

    # TODO: figure out how to let user select starting square
    # TODO: make '63' as limit in knightTour dynamic
    knightsTour = gkt.knightTour(0,knightsPath,knightsGraph.getVertex(4),searchLimit)



    # for vert in knightsTour:
    #     print(vert.getId())

    # TODO: uncomment to display chessboard
    # Now I have a nice dictionary with all my squares

    vs = {}
    squares = genSquares(bSize)
    i = 0
    for key in squares:
        # print(type(squares[key]))
        vs[i] = squares[key]
        label = Text(squares[key].getCenter(),str(key) + " " + str(i))
        i = i + 1
        
        squares[key].draw(bWin)
        label.draw(bWin)

    # Manually undraw, setfill, and redraw
    # TODO: make a method that does this for 'visited'
    for vert in knightsTour:
        sqId = vert.getId()
        if sqId in vs.keys():
            # print(sqId)
            # print(vs[sqId])
            time.sleep(.4)
            vs[sqId].undraw()
            vs[sqId].setFill('brown')
            vs[sqId].draw(bWin)

            #Draw some lines
            # if sqId > 0:
            #     mL = Line(vs[sqId].getCenter(),vs[sqId].getCenter())
            #     mL.setFill('Blue')
            #     mL.draw(bWin)


    # print(squares['a1'])
    # squares['a1'].undraw()
    # squares['a1'].setFill('red')
    # squares['a1'].draw(bWin)


    # Line experiment
    #  TODO: Method to draw line between vertices as they are traversed
    # mL = Line(squares['a1'].getCenter(),squares['c8'].getCenter())
    # mL.setFill('red')
    # mL.draw(bWin)

    # TODO: Handle getmouse
    bWin.getMouse()
main()
