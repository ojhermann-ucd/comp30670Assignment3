#puts the Instruction into the desired format
def instructionFormat(str):
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")] #replace useless strings
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split() #turn it from string to list
    return str

#determines if the Instruction is valid
def instructionValid(theList):
    if len(theList) != 5: #all valid Instructions are of length 5
        return False
    if theList[0] not in ["off", "on", "switch"]: #all valid instructions begin with one of these Commands
        return False
    for i in range(1, 5, 1): # all valid instructions have four integer inputs
        try:
            if not isinstance(int(theList[i]), int):
                return False
        except ValueError:
            return False
    return True

#makes sure the integer values are within acceptable ranges
def instructionValidRange(theList, upperBound):
    for i in range(1, 5, 1):
        theList[i] = str(max(0, int(theList[i])))
        theList[i] = str(min(int(theList[i]), upperBound))
    return theList

#makes sure that x1<=x2 and y1<=y2
def instructionValidOrder(theList):
    return (int(theList[1]) <= int(theList[3]) and int(theList[2]) <= int(theList[4]))

#converts the Instruction into a form amenable to modifying the Grid
def instructionForm(theList):
    command = theList[0]
    commandStart = (int(theList[1]), int(theList[2]))
    commandEnd = (int(theList[3]), int(theList[4]))
    return [command, commandStart, commandEnd]