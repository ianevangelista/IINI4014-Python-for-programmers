import turtle
import math
import time

# Converting from degrees to get the x-position 
def convertToPosX(radius, xPos):
    return (radius * math.sin(math.pi*2*xPos / 360))

# Converting from degrees to get the y-position 
def convertToPosY(radius, yPos):
    return (radius * math.cos(math.pi*2*yPos / 360))

# Task 1
def timesTable(radius, totPoints, multiplier, myTurtle):
    # Starting position
    xPos = -180
    yPos = 0
    xCord = xPos
    yCord = yPos
    myTurtle.up()
    myTurtle.goto(xCord, yCord)
    # Finds the degree per point
    degreesPerPoint = 360 / totPoints

    # Drawing all lines
    for point in range(totPoints):
        point += 1
        xPos -= degreesPerPoint
        yPos += degreesPerPoint

        # Finds next point and goes to it
        xCord = convertToPosX(radius, xPos)
        yCord = convertToPosY(radius, yPos)
        myTurtle.goto(xCord, yCord)

        # Putting pen down
        myTurtle.pd()

        # Finds the multiplied end-point
        endP = point * multiplier
        endXpos = (-180 + (endP*degreesPerPoint))
        endYpos = (-180 + (endP*degreesPerPoint))
        endPointX = convertToPosX(radius, endXpos)
        endPointY = convertToPosY(radius, endYpos)
        
        # Drawing line to the multiplied end-point
        myTurtle.goto(endPointX, endPointY)
        myTurtle.up()

# Task 2
def genEndPoints(radius, totPoints, degreesPerPoint, multiplier):
    # Finds the multiplied end-point
    for point in range(totPoints):
        point += 1
        endP = point * multiplier
        endXpos = (-180 + (endP*degreesPerPoint))
        endYpos = (-180 + (endP*degreesPerPoint))

        # Yields the multiplied end-points
        yield convertToPosX(radius, endXpos)
        yield convertToPosY(radius, endYpos)

def timesTableGenerator(radius, totPoints, multiplier, myTurtle):
    # Starting position
    xPos = -180
    yPos = 0
    xCord = xPos
    yCord = yPos
    myTurtle.up()
    myTurtle.goto(xCord, yCord)
    degreesPerPoint = 360 / totPoints

    # Creating an iterator-object
    generator = genEndPoints(radius, totPoints, degreesPerPoint, multiplier)

    for nextPoint in range(totPoints):
        nextPoint += 1
        xPos -= degreesPerPoint
        yPos += degreesPerPoint

        xCord = convertToPosX(radius, xPos)
        yCord = convertToPosY(radius, yPos)
        myTurtle.goto(xCord, yCord)
        myTurtle.pd()

        # Drawing line to the multiplied end-point
        myTurtle.goto(next(generator), next(generator))
        myTurtle.up()

def main():
    myWindow = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    start = time.time()
    #timesTable(300, 200, 2, t)
    timesTableGenerator(300, 200, 2, t)
    end = time.time()

    # Printing out the time and converting it to ms  
    # TimesTable(): 15656 ms 
    # TimesTableGenerator(): 15309 ms 
    print((end - start)*1000)
    myWindow.exitonclick()
  
main()