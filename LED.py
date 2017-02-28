#imports
import sys
import Grid
import Instructions
import Modification
import Links
import urllib.request
from urllib.error import URLError, HTTPError

#create sourceList
sourceList = Links.createLinkList("LinksSource.txt")

#create gridSizeList
gridSizeList = Grid.gridCreateSizeList(sourceList)

#create grids
testGrid = Grid.Grid(gridSizeList[0]).grid