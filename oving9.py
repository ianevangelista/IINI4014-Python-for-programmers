from graphics import *
import random


class Die():

    def __init__(self, size, xPos, yPos, colorDie='white', colorDot='black'):
        self.size = size
        self.xPos = xPos
        self.yPos = yPos
        self.colorDie = colorDie
        self.colorDot = colorDot
        self.dots = 0

    def createDie(self, win):
        rect = Rectangle(Point(self.xPos, self.yPos), Point(
            self.xPos+self.size, self.yPos+self.size))
        rect.setFill(self.colorDie)
        rect.draw(win)
    '''
    Function that creates the die
    Takes:
    win: window: the window
    '''

    def getDots(self):
        return self.dots
    '''
    Function that return the value you get when rolling the die
    Return:
    self.dot: int: the amount of dots
    '''

    def getPosition(self):
        return (self.xPos, self.yPos)
    '''
    Function that return the position of the die
    Return:
    (self.xPos, self.yPos): x,y: the x and y position of the die
    '''

    def getSize(self):
        return self.size
    '''
    Function that return the size the die
    Return:
    self.size: int: the size of the die
    '''

    def rollDie(self):
        # Creating a window
        win = GraphWin("Assignment 9", 500, 500)
        win.setBackground('white')

        # Creating the die
        self.createDie(win)

        # Getting a random amount of dots from 1-6
        dots = random.randrange(1, 7)
        # Setting the value of the dots
        self.dots = dots

        # Checking the value of dots to draw
        if dots == 1:
            # Creating a circle, fill it and draw it
            cir = Circle(Point(self.xPos + self.size/2,
                               self.yPos+self.size/2), self.size//10)
            cir.setFill(self.colorDot)
            cir.draw(win)

        elif dots == 2:
            cir1 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+self.size/2), self.size//10)
            cir2 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+self.size/2), self.size//10)
            cir1.setFill(self.colorDot)
            cir2.setFill(self.colorDot)
            cir1.draw(win)
            cir2.draw(win)

        elif dots == 3:
            cir1 = Circle(Point(self.xPos + self.size/4,
                                self.yPos+self.size/4), self.size//10)
            cir2 = Circle(Point(self.xPos + (self.size/4)*2,
                                self.yPos+(self.size/4)*2), self.size//10)
            cir3 = Circle(Point(self.xPos + (self.size/4)*3,
                                self.yPos+(self.size/4)*3), self.size//10)

            cir1.setFill(self.colorDot)
            cir2.setFill(self.colorDot)
            cir3.setFill(self.colorDot)
            cir1.draw(win)
            cir2.draw(win)
            cir3.draw(win)

        elif dots == 4:
            cir1 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+self.size/3), self.size//10)
            cir2 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+self.size/3), self.size//10)

            cir3 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+(self.size/3)*2), self.size//10)
            cir4 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+(self.size/3)*2), self.size//10)

            cir1.setFill(self.colorDot)
            cir2.setFill(self.colorDot)
            cir3.setFill(self.colorDot)
            cir4.setFill(self.colorDot)
            cir1.draw(win)
            cir2.draw(win)
            cir3.draw(win)
            cir4.draw(win)

        elif dots == 5:
            cir1 = Circle(Point(self.xPos + self.size/4,
                                self.yPos+self.size/4), self.size//10)
            cir2 = Circle(Point(self.xPos + (self.size/4)*2,
                                self.yPos+(self.size/4)*2), self.size//10)
            cir3 = Circle(Point(self.xPos + (self.size/4)*3,
                                self.yPos+(self.size/4)*3), self.size//10)
            cir4 = Circle(Point(self.xPos + (self.size/4)*3,
                                self.yPos+self.size/4), self.size//10)
            cir5 = Circle(Point(self.xPos + self.size/4,
                                self.yPos+(self.size/4)*3), self.size//10)

            cir1.setFill(self.colorDot)
            cir2.setFill(self.colorDot)
            cir3.setFill(self.colorDot)
            cir4.setFill(self.colorDot)
            cir5.setFill(self.colorDot)
            cir1.draw(win)
            cir2.draw(win)
            cir3.draw(win)
            cir4.draw(win)
            cir5.draw(win)

        else:
            cir1 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+self.size/4), self.size//10)
            cir2 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+self.size/4), self.size//10)

            cir3 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+(self.size/4)*2), self.size//10)
            cir4 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+(self.size/4)*2), self.size//10)

            cir5 = Circle(Point(self.xPos + self.size/3,
                                self.yPos+(self.size/4)*3), self.size//10)
            cir6 = Circle(Point(self.xPos + (self.size/3)*2,
                                self.yPos+(self.size/4)*3), self.size//10)

            cir1.setFill(self.colorDot)
            cir2.setFill(self.colorDot)
            cir3.setFill(self.colorDot)
            cir4.setFill(self.colorDot)
            cir5.setFill(self.colorDot)
            cir6.setFill(self.colorDot)
            cir1.draw(win)
            cir2.draw(win)
            cir3.draw(win)
            cir4.draw(win)
            cir5.draw(win)
            cir6.draw(win)

        win.getMouse()
        win.close()

    '''
    Function that rolls the die and draws the circles
    '''


def main():
    # Input for size, positon and colors
    inputSize = int(input("What size do you wish? "))
    inputXpos = int(input("What X-position do you wish? "))
    inputYpos = int(input("What Y-position do you wish? "))
    inputCustomColors = input("Do you wish custom colors? Answer yes or no ")

    if inputCustomColors == 'yes':
        inputColorDie = input("What color do you wish the die should be? ")
        inputColorDots = input("What color do you wish the dots should be? ")
        myDie = Die(inputSize, inputXpos, inputYpos,
                    inputColorDie, inputColorDots)
        myDie.rollDie()

    else:
        myDie = Die(inputSize, inputXpos, inputYpos)
        myDie.rollDie()

    print("My value:", myDie.getDots())
    print("Position:", myDie.getPosition())
    print("Size of die:", myDie.getSize())


main()
