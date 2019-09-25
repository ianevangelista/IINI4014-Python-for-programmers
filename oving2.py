# Øving 2
import math
# Start-value of the amount of sides
nSides = 6 
# Start-value of the length of the side
sLength = 1 
# The length of the range
length = 25

def ArchimedesPI(nSides, sLength):
    for x in range(length):
        n = nSides
        S = sLength
        S2 = S/2
        a = math.sqrt(1-S2**2)
        b = 1-a
        newS = math.sqrt(b**2+S2**2)
        P = n*S
        pi = P/2
        # Increasing the amount of sides by multiplying 2
        nSides *= 2
        # Sets a new length to the sides from the previous calculation
        sLength = newS
        # Formatting the output with 14 decimals
        print(f'pi is {pi:.14f}')
        
ArchimedesPI(nSides, sLength)