from Cylinder import Cylinder
from Arc import Arc
from Line import Line
from Swept import Swept
from math import cos, sin
import math

side = 5
div = 15

offset = 0.05
circular_pitch = side*4+ offset
teeth = 10

pitch_dia = teeth * circular_pitch/math.pi

dia= pitch_dia - (div)
radius = dia / 2

height = 10


x0= -side
y0 = radius
x1 = -side
y1 = (radius + div/2)
x2 = -side/2
y2 = radius + div
x3 = side/2
y3 = radius + div
x4 = side
y4 = radius + div / 2
x5 = side
y5 = radius

# Create the gear-like shape
gear_shape = Cylinder(0, 0, 0, dia, height)  # Start with a cylinder

for i in range(teeth):
    line1 = Line(x0, y0, 0, x1, y1, 0)
    line2 = Line(x1, y1, 0, x2, y2, 0)
    line3 = Line(x2, y2, 0, x3, y3, 0)
    line4 = Line(x3, y3, 0, x4, y4, 0)
    line5 = Line(x4, y4, 0, x5, y5, 0)
    line6 = Line(x5, y5, 0, x0, y0, 0)

    arc = Arc(-side, radius, 0, [1, 0, 0], [0, 1, 0], radius, 0, math.atan(side*2/dia))
    line8 = Line(x5, y5, 0, x0, y0, 0)
    
    sec = [line1, line2, line3, line4, line5, line6]

    line7 = Line(0, radius - side / 2, 0, 0, radius - side / 2, height)
    swept = Swept([line7], sec, 0, 0, 0, dia, height)

    sec_arc = [arc, line8]
    #swept_arc = Swept([line7], sec_arc, 0, 0, 0, dia, height)
    #swept.subtract(swept_arc)


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

    zline2 = Line(0, radius + div/2, 0, 0, radius + div/2, height)
    zline2 = zline2.rotate(angle)

    swept2 = Swept([zline2], section, 0, 0, 0, dia, height)

