#Tye Hickman
#Week 3 Review
#My AWESOME House
import graphics as g
from graphics import *
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
clicksLeft = 10
isOpen = True
signMessage = 'Open' if isOpen else 'Closed'
countDown = Text(Point(275,175),clicksLeft)

roof = Polygon(Point(40,100),Point(200,20),Point(360,100))
roof.setOutline('red')
roof.setFill('red')
decoLineA = Line(Point(50,105,),Point(200,30))
decoLineB = Line(Point(200,30),Point(350,105))
roofA = Line(Point(50,100), Point(200,50))
roofB = Line(Point(200,50),Point(350,100))
walls = Rectangle(Point(50,100),Point(350,350))
walls.setOutline('gray')
walls.setFill('cyan')
window = Circle(Point(275,175), 25)
window.setOutline('yellow')
window.setFill('yellow')
openSign = Text(Point(125,175),signMessage)
openSign.setTextColor('blue')

door = Rectangle(Point(100,245),Point(200,350))
door.setFill('brown')
door.setOutline('brown')
def drawHouse():
    roof.draw(win)
    decoLineA.draw(win)
    decoLineB.draw(win)
    walls.draw(win)
    window.draw(win)
    door.draw(win)
    openSign.draw(win)
    countDown.draw(win)

win = g.GraphWin("My House",WINDOW_WIDTH,WINDOW_HEIGHT)
win.setBackground('purple')
drawHouse()
for i in range(clicksLeft):
    win.getMouse()
    isOpen = not isOpen
    signMessage = 'Open' if isOpen else 'Closed'
    colorWin = 'yellow' if isOpen else 'black'
    colorBack = 'gray' if isOpen else 'black'
    clicksLeft = clicksLeft-1
    print(isOpen)
    print(clicksLeft)
    win.setBackground(colorBack)
    openSign.setText(signMessage)
    window.setFill(colorWin)
    countDown.setText(clicksLeft)