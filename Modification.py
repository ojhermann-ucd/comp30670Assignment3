testGrid = {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}

testInstruction = ["switch", (1,1), (2, 2)]

def modificationCommand(theList): #list input
    return theList[0] #str output

#generate the startTuple
def modificationTupleStart(theList): #list input
    return theList[1] #tuple output

#generate the endtTuple
def modificationTupleEnd(theList): #list input
    return theList[2] #tuple output

def modificationModificationMicro(theCommand, theBool):
    if theCommand == "on":
        return True
    if theCommand == "off":
        return False
    if theCommand == "switch":
        if theBool == True:
            return False
        else:
            return True

def modificationModification(theList, theGrid): #input list and dictionary
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