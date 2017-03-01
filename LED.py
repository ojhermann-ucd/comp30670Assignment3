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
import argparse
from builtins import str

#argparse stuff
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-i", "--input", action="store_true")
#group.add_argument("-f", "--file", action="store_true")

parser.add_argument("source", help="a valid url")
args = parser.parse_args()

"""
if args.url:
    sourceList = []
    sourceList.append(args.source)
else:
    sourceList = Links.createLinkList(str(args.source))
"""

#sourceList = Links.createLinkList("LinksSource.txt")

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



#create sourceList
if Links.validLink(args.source):
    sourceList = []
    sourceList.append(args.source)
    #create gridSizeList
    gridSizeList = Grid.gridCreateSizeList(sourceList)
    #do it
    count = 0
    for g in gridSizeList:
        #startTime = time.time()
        if g == "n/a":
            print(sourceList[count], g)
        else:
            print(sourceList[count], sumLED(int(g), sourceList[count]))
            #print(time.time() - startTime)
        count += 1
else:
    print("That was not a valid url")