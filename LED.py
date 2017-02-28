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

#execute instructions
theSource = sourceList[0]
theSource = urllib.request.urlopen(theSource)
for line in theSource:
    theLine = str(line, 'utf-8')
    print(theLine)

"""
theSource = theSource.readlines()
print(type(theSource[1]))
print(theSource[1])
theSource[1] = str(theSource[1], 'utf-8')
print(type(theSource[1]))
print(theSource[1])
"""