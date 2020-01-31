from tkinter import *
import random


class Die():

    def __init__(self, size, xPos, yPos, colorDie='white', colorDot='black'):
        self.size = size
        self.xPos = xPos
        self.yPos = yPos
        self.colorDie = colorDie
        self.colorDot = colorDot
        self.dots = 0

    def getDots(self):
        '''
        Function that return the value you get when rolling the die
        Return:
        self.dot: int: the amount of dots
        '''
        return self.dots

    def getPosition(self):
        '''
        Function that return the position of the die

        Return:
        (self.xPos, self.yPos): x,y: the x and y position of the upper left corner of the die
        '''
        return (self.xPos, self.yPos)

    def getSize(self):
        '''
        Function that return the size the die

        Return:
        self.size: int: the size of the die
        '''
        return self.size

    def createDie(self, canvas):
        '''
        Function that creates the rectange of the die

        Takes:
        canvas: canvas: the canvas where rectangle is drawn

        '''
        canvas.create_rectangle(
            self.xPos, self.yPos, self.xPos+self.size, self.yPos+self.size, fill=self.colorDie)

    def drawDie(self, canvas):
        '''
        Function that rolls the die and draws the circles

        Takes:
        canvas: canvas: the canvas where the dots are drawn
        '''

        # Draws the square
        self.createDie(canvas)
        # Getting a random amount of dots from 1-6
        dots = random.randrange(1, 7)
        # Setting the value of the dots
        self.dots = dots

        # Variables to use for dots in the center
        xMid = self.xPos + self.size/2
        yMid = self.yPos + self.size/2

        # Checking the value of dots to draw
        if dots == 1:
            # Creating a circle, fill it and draw it

            canvas.create_oval(xMid - self.size/10, yMid - self.size/10,
                               xMid + self.size/10, yMid + self.size/10, fill=self.colorDot)

        elif dots == 2:

            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+self.size/2 - self.size/10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+self.size/2 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+self.size/2 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+self.size/2 + self.size/10, fill=self.colorDot)

        elif dots == 3:
            canvas.create_oval(self.xPos + self.size/4 - self.size/10,
                               self.yPos+self.size/4 - self.size/10, self.xPos + self.size/4 + self.size/10,
                               self.yPos+self.size/4 + self.size/10, fill=self.colorDot)

            canvas.create_oval(xMid - self.size/10, yMid - self.size/10,
                               xMid + self.size/10, yMid + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/4)*3 - self.size/10,
                               self.yPos + (self.size/4)*3 - self.size /
                               10, self.xPos + (self.size/4)*3 + self.size/10,
                               self.yPos + (self.size/4)*3 + self.size/10, fill=self.colorDot)

        elif dots == 4:
            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+self.size/3 - self.size/10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+self.size/3 + self.size/10, fill=self.colorDot)
            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+self.size/3 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+self.size/3 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+(self.size/3)*2 - self.size /
                               10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+(self.size/3)*2 + self.size/10, fill=self.colorDot)
            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+(self.size/3)*2 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+(self.size/3)*2 + self.size/10, fill=self.colorDot)

        elif dots == 5:
            canvas.create_oval(self.xPos + self.size/4 - self.size/10,
                               self.yPos+self.size/4 - self.size/10, self.xPos + self.size/4 + self.size/10,
                               self.yPos+self.size/4 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/4)*3 - self.size/10,
                               self.yPos+(self.size/4)*3 - self.size /
                               10, self.xPos + (self.size/4)*3 + self.size/10,
                               self.yPos+(self.size/4)*3 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/4)*3 - self.size/10,
                               self.yPos+self.size/4 - self.size /
                               10, self.xPos + (self.size/4)*3 + self.size/10,
                               self.yPos+self.size/4 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + self.size/4 - self.size/10,
                               self.yPos+(self.size/4)*3 - self.size /
                               10, self.xPos + self.size/4 + self.size/10,
                               self.yPos+(self.size/4)*3 + self.size/10, fill=self.colorDot)

            canvas.create_oval(xMid - self.size/10, yMid - self.size/10,
                               xMid + self.size/10, yMid + self.size/10, fill=self.colorDot)

        else:
            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+self.size/4 - self.size/10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+self.size/4 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+self.size/4 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+self.size/4 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+(self.size/4)*2 - self.size /
                               10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+(self.size/4)*2 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+(self.size/4)*2 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+(self.size/4)*2 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + self.size/3 - self.size/10,
                               self.yPos+(self.size/4)*3 - self.size /
                               10, self.xPos + self.size/3 + self.size/10,
                               self.yPos+(self.size/4)*3 + self.size/10, fill=self.colorDot)

            canvas.create_oval(self.xPos + (self.size/3)*2 - self.size/10,
                               self.yPos+(self.size/4)*3 - self.size /
                               10, self.xPos + (self.size/3)*2 + self.size/10,
                               self.yPos+(self.size/4)*3 + self.size/10, fill=self.colorDot)

    def rollDie(self):
        '''
        Function that creates two canvases: one for input and one for the die
        '''
        # Creating a window
        window = Tk()
        inputCanvas = Canvas(window, width=300, height=900, background='white')
        canvas = Canvas(window, width=800, height=900, background='white')
        inputCanvas.grid(row=0, column=0)
        canvas.grid(row=0, column=1)

        # Creating the die when pressing the button
        def btnFuntction():
            '''
            Function that rolls and draw the die. Gets input from the user
            '''

            # Deleting the previous die
            canvas.delete(ALL)

            resX = int(entryX.get())
            resY = int(entryY.get())
            resSize = int(entrySize.get())
            resColorDie = entryColorDie.get()
            resColorDots = entryColorDots.get()
            self.xPos = resX
            self.yPos = resY
            self.size = resSize
            self.colorDie = resColorDie
            self.colorDot = resColorDots
            self.drawDie(canvas)

        # Input for the user
        Label(inputCanvas, text='X-position: ').grid(row=0)
        entryX = Entry(inputCanvas)
        entryX.grid(row=0, column=1)
        entryX.insert(0, 250)

        Label(inputCanvas, text='Y-position: ').grid(row=1)
        entryY = Entry(inputCanvas)
        entryY.grid(row=1, column=1)
        entryY.insert(0, 250)

        Label(inputCanvas, text='Size: ').grid(row=2)
        entrySize = Entry(inputCanvas)
        entrySize.grid(row=2, column=1)
        entrySize.insert(0, 200)

        Label(inputCanvas, text='Color of die: ').grid(row=3)
        entryColorDie = Entry(inputCanvas)
        entryColorDie.grid(row=3, column=1)
        entryColorDie.insert(0, 'white')

        Label(inputCanvas, text='Color of dots: ').grid(row=4)
        entryColorDots = Entry(inputCanvas)
        entryColorDots.grid(row=4, column=1)
        entryColorDots.insert(0, 'black')
        btn = Button(inputCanvas,
                     text='Submit', command=btnFuntction)
        btn.grid(row=5, column=0)

        window.mainloop()


def main():

    myDie = Die(200, 200, 200)
    myDie.rollDie()


main()
