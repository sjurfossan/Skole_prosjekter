from Cylinder import Cylinder
from Arc import Arc
from Line import Line
from Swept import Swept
from math import cos, sin, tan, asin
import math




def Drive_Shaft(x, y, z, radius, length, direction):
    
    cyl = Cylinder(x, y, z, radius*2, length, direction)

    lock_line_1 = Line((x+radius*0.1), -(y+cos(asin((x+radius*0.1)/radius))*radius), z, (x+radius*0.1), -(y+radius*1.1), z)
    lock_line_2 = Line((x+radius*0.1), -(y+radius*1.1), z, -(x+radius*0.1), -(y+radius*1.1), z)
    lock_line_3 = Line(-(x+radius*0.1), -(y+radius*1.1), z, -(x+radius*0.1), -(y+cos(asin((x+radius*0.1)/radius))*radius), z)
    lock_line_4 = Line(-(x+radius*0.1), -(y+cos(asin((x+radius*0.1)/radius))*radius), z, (x+radius*0.1), -(y+cos(asin((x+radius*0.1)/radius))*radius), z)

    section = [lock_line_1, lock_line_2, lock_line_3, lock_line_4]

    lock_guide_line = Line(0, 0, 0, 0, 0, length)

    body = Swept([lock_guide_line], section, 0, 0, 0, 0, 0)


    return cyl, body


def main():
    Drive_Shaft(0, 0, 0, 20, 200, [0, 0, 1])

main()