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

def gridCheckIntSize(theInt):
    return (theInt < 10**9)

class Grid: #creates the grid with initial values of False

    #in program: use input mechanism to check for integer inputs
    #in program: use input mechanism to check for positive entries
    def __init__(self, num):
        self.rows = int(num)
        self.columns = int(num)
        self.grid = self.generateGrid()
        self.size = (int(num) + 1) ** 2 #used in testing

    def generateGrid(self): #add value range penalty
        theGrid = {}
        row = 0
        column = 0
        while row <= self.rows:
            while column <= self.columns:
                theGrid[(row, column)] = False
                column += 1
            column = 0
            row += 1

        return theGrid
    
aGrid = Grid(0)
print(aGrid.grid)