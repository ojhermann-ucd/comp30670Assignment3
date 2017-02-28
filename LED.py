#imports
import sys
import Grid
import Instructions
import Modification
import Links
import urllib.request
from urllib.error import URLError, HTTPError
from itertools import islice
import io

#create sourceList
sourceList = Links.createLinkList("LinksSource.txt")

#create gridSizeList
gridSizeList = Grid.gridCreateSizeList(sourceList)

#create grids
testGrid = Grid.Grid(gridSizeList[0]).grid

def sumLED(gridSize, theSource): #int, str
    theGrid = Grid.Grid(gridSize).grid
    theSource = urllib.request.urlopen(theSource)
    for line in theSource:
        theLine = str(line, 'utf-8')
        #formatting
        theLine = Instructions.instructionFormat(theLine)
        #test
        if not Instructions.instructionValidTypes(theLine):
            pass
        else:
            theLine = Instructions.instructionValidRange(theLine, gridSize)
            if not Instructions.instructionValidOrder(theLine):
                pass
            else:
                theLine = Instructions.Instruction(theLine)
                theGrid = Modification.modificationGrid(theLine, theGrid)
                gridSum = sum(theGrid.values())
    return gridSum

print(sumLED(int(gridSizeList[0]), sourceList[0]))


#execute instructions
theUpperBound = int(gridSizeList[0])
theSource = sourceList[0]
theSource = urllib.request.urlopen(theSource)
for line in theSource:
    theLine = str(line, 'utf-8')
    #formatting
    theLine = Instructions.instructionFormat(theLine)
    #test
    if not Instructions.instructionValidTypes(theLine):
        pass
    else:
        theLine = Instructions.instructionValidRange(theLine, theUpperBound)
        if not Instructions.instructionValidOrder(theLine):
            pass
        else:
            theLine = Instructions.Instruction(theLine)
            testGrid = Modification.modificationGrid(theLine, testGrid)
gridSum = sum(testGrid.values())
print(gridSum)