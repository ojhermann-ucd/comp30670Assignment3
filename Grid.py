#turns input into a list after removing leading whitespace
def gridInputRemoveLeftWhiteSpace(str): #string input
    str = str.lstrip()
    str = str.split() 
    return str #returns a list

#checks if length is one i.e. only one number was given
def gridCheckLength(theList): #list input
    return (len(theList) == 1) #boolean output

#checks if the entry is a number
def gridCheckInt(theList): #list input
    return isinstance(int(theList[0]), int) #boolean output

#generates the integer
def gridMakeInt(theList): #list input
    return int(theList[0]) #int output

#makes sure theInt is positive
def gridCheckIntSign(theInt): #int input
    return (theInt > -1) #boolean output

#generates the grid as a dictionary of (x, y) : boolean key : value pairs
def gridMakeGrid(theInt): #int input
    row = 0
    column = 0
    theGrid = {}
    while row <= theInt:
        while column <= theInt:
            theGrid[(row, column)] = False
            column += 1
        column = 0
        row += 1
    return theGrid #dict output