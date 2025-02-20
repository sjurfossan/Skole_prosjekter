
from motion import Motion2
from motion3 import Motion3
from gear import Gear
from Shapes.Arc import Arc
from Shapes.Line import Line
from Shapes.Swept import Swept


from other.filesaver import FileSaver
import random

#User choose the values
ratio = 1
numberOfGears = 2
diameter = 20
module = 0.7
height = 5

#x, y, z, = 0, 0, 0


gears = []

for i in range(0,numberOfGears):
    if (i%2 == 0):
        gear = Gear(mod = module, disk_dia = diameter*ratio, disk_height = height, const = 0, y_diff = i*(diameter/2 + diameter*ratio/2))
        #add gear to list
        gears.append(gear)
    else:
        gear = Gear(mod = module, disk_dia = diameter, disk_height = height, const = 1, y_diff = i*(diameter/2 + diameter*ratio/2))
        #add gear to list
        gears.append(gear)


fileName = "geartrain_" + str(random.randint(1,10000)) 
pathToTheFolder = "C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 2\\tmm4220-assignment2\\Animations\\"

fileSaver = FileSaver(pathToTheFolder, fileName)
motion = Motion3(fileName, pathToTheFolder)
#motion = Motion3(gears, 0, 10, 10, 0, True, pathToTheFolder, fileName)

