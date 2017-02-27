#turns input into a list after removing leading whitespace
def gridInputRemoveLeftWhiteSpace(str):
    str = str.lstrip()
    str = str.split() 
    return str #returns a list

#checks if length is one i.e. only one number was given
def gridCheckLength(theList):
    return (len(theList) == 1)

#checks if the entry is a number
def gridCheckInt(theList):
    return isinstance(int(theList[0]), int)

#generates the integer
def gridMakeInt(theList):
    return int(theList[0])

def gridMakeGrid(theInt):
    row, column = 0, 0
    theGrid = {}
    while row <= theInt:
        while column <= theInt:
            theGrid[(row, colum)] = False
            column += 1
        column = 0
    row += 1
    return theGrid

