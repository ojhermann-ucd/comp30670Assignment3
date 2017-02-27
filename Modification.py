from Grid import *
from Instructions import *

testGrid = {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}

testInstruction = ["switch", 1, 1, 2, 2]

def modificationEntry(theI, theBool): #Instruction and boolean inputs
    if theI.command == "on":
        return True
    if theI.command == "off":
        return False
    if theI.command == "switch":
        return not theBool

def modificationGrid(theI, theG): #instuctions and grid
    for x in range(theI.x1, theI.x2 + 1, 1):
        for y in range(theI.y1, theI.y2 + 1, 1):
            xyTuple = (x, y)
            xyBool = theG.get(xyTuple,)
            theG[xyTuple] = modificationEntry(theI, xyBool)
    return theG

print(modificationGrid(Instruction(testInstruction), testGrid))

"""    
    #variables
    theCommand = theList[0]
    xStart = theList[1][0]
    yStart = theList[1][1]
    xEnd = theList[2][0]
    yEnd = theList[2][1]
    
    #modification
    for x in range(xStart, xEnd + 1, 1):
        for y in range(yStart, yEnd + 1, 1):
            theTuple = (x, y)
            theBool = theGrid.get(theTuple,)
            theGrid[theTuple] = modificationModificationMicro(theCommand, theBool)
    return theGrid #output dictionary
"""