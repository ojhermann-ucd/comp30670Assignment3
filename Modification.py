testGrid = {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}

testInstruction = ["switch", (1,1), (2, 2)]


#generate the startTuple
def modificationTupleStart(theList): #list input
    return theList[1] #tuple output

#generate the endtTuple
def modificationTupleEnd(theList): #list input
    return theList[2] #tuple output