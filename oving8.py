from graphics import *


def createCirles(color, win, width, sizeWindow, size):
    xPos = 10
    yPos = 10
    counterX = 1
    counterY = 1
    for circle in range(sizeWindow):
        circle = Circle(Point(xPos * counterX, yPos*counterY), width/2)
        circle.setFill(color)
        circle.setOutline(color)
        circle.draw(win)
        # print('xpos*counterx:', (xPos*counterX),
        #      'ypos*countery', (yPos*counterY))
        counterX += size

        if (xPos*counterX) >= sizeWindow:
            counterY += size
            counterX = 1


'''
Function that creates circles
Takes:
color: string: color of the circles
win: window: the window
width: int: diameter of the circle
sizeWindow: int: the window-size
size: int: size of the squares to know where to place the circles
'''


def createLines(color, size, win, width, sizeWindow):
    counter = 1
    for line in range(sizeWindow//size):
        vertStartPoint = Point(10 * counter, 0)
        vertEndPoint = Point(10 * counter, sizeWindow)
        vertLine = Line(vertStartPoint, vertEndPoint)
        vertLine.setWidth(width)
        vertLine.setFill(color)

        horizStartPoint = Point(0, 10 * counter)
        horizEndPoint = Point(sizeWindow, 10 * counter)
        horizLine = Line(horizStartPoint, horizEndPoint)
        horizLine.setWidth(width)
        horizLine.setFill(color)
        counter += size

        vertLine.draw(win)
        horizLine.draw(win)


'''
Function that creates lines
Takes:
color: string: color of the lines
size: int: size of the squares
win: window: the window
width: int: width of the line
sizeWindow: int: the window-size
'''


def hermannGrid(colorSquare, colorLine, colorCircles, sizeWindow, sizeSquare, widthLine):
    win = GraphWin("sirkel", sizeWindow, sizeWindow)
    win.setBackground(colorSquare)
    createLines(colorLine, sizeSquare, win, widthLine, sizeWindow)
    createCirles(colorCircles, win, widthLine, sizeWindow, sizeSquare)

    win.getMouse()
    win.close()


'''
Function that creates the Hermann Grid illusion 
Takes:
colorSquare: string: color of the square 
colorLine: string: color of the lines 
colorCircles: string: color of the circles 
sizeWindow: int: the window-size
sizeSquare: int: size of the squares
widthLine: int: the width of the lines
'''


hermannGrid('black', 'grey', 'white', 500, 10, 10)
