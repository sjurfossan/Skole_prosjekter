from Cylinder import Cylinder
from Line import Line
from Swept import Swept
from math import cos, sin
import math

dia = 100
side = 10
radius = dia / 2
height = 10
teeth = 15
div = 10
inner_dia = 75
pitch_dia = 87.5
center_dist = 100
shaft_dia = 15
shaft_length = 50

gear_shape = Cylinder(0, 0, 0, dia, height)
shaft = Cylinder(0, 0, -shaft_length/2, shaft_dia, shaft_length)

x0= -side
y0 = radius
x1 = -side/2-div/3
y1 = radius - div/2
x2 = -side/2
y2 = radius - div
x3 = side/2
y3 = radius - div
x4 = side/2+div/3
y4 = radius - div/2
x5 = side
y5 = radius


line1 = Line(x0, y0, 0, x1, y1, 0)
line2 = Line(x1, y1, 0, x2, y2, 0)
line3 = Line(x2, y2, 0, x3, y3, 0)
line4 = Line(x3, y3, 0, x4, y4, 0)
line5 = Line(x4, y4, 0, x5, y5, 0)
line6 = Line(x5, y5, 0, x0, y0, 0)

#add the lines to the section
sec = [line1, line2, line3, line4, line5, line6]

#make swept line
zline = Line(0, y1, 0, 0, y1, height)

def rotate_lines_around_origin(lines, angle):
    """Rotates the given lines around the origin by the given angle in degrees."""
    rotated_lines = []
    for line in lines:
        rotated_lines.append(line.rotate(angle))
    return rotated_lines

def get_angles(x):
  angles = []
  for i in range(x):
    angle = (2 * math.pi * i) / x
    angles.append(angle)
  return angles

for i in range (teeth):
    angle = get_angles(teeth)[i]
    section = rotate_lines_around_origin(sec, angle)

    zline2 = Line(0, y1, 0, 0, y1, height)
    zline2 = zline2.rotate(angle)

    swept2 = Swept([zline2], section, 0, 0, 0, dia, height)
    gear_shape.subtract(swept2)