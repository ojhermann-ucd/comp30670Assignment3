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
import time

#create sourceList
sourceList = Links.createLinkList("LinksSource.txt")

#create gridSizeList
gridSizeList = Grid.gridCreateSizeList(sourceList)

#function for summing the values of the grid
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

#do it
count = 0
for g in gridSizeList:
    startTime = time.time()
    if g == "n/a":
        print(sourceList[count], g)
    else:
        print(sourceList[count], sumLED(int(g), sourceList[count]))
        print(time.time() - startTime)
    count += 1