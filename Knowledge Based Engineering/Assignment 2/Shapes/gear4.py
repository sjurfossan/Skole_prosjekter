from Cylinder import Cylinder
from Line import Line
from Swept import Swept
import math

x = 12

def get_angles(x):
  angles = []
  for i in range(x):
    angle = (2 * math.pi * i) / x
    angles.append(angle)
  return angles

angles = get_angles(x)

center_x = 0
center_y = 0
radius = 10

for angle in angles:
  x0 = center_x + radius * math.cos(angle)
  y0 = center_y + radius * math.sin(angle)
  x1 = center_x
  y1 = center_y

  line = Line(x0, y0, 0, x1, y1, 0)
