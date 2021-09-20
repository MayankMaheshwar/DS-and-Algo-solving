from geektrust import Room
import sys


if len(sys.argv) != 2:
    raise ValueError('Please provide input file to test the code.')

cCave = Room("C-Cave", 3)
dTower = Room("D-Tower", 7)
gMansion = Room("G-Mansion", 20)

print(cCave.timeList)
