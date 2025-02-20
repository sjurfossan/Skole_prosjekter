from Cylinder import Cylinder
from Arc import Arc
from Line import Line
from Swept import Swept
from math import cos, sin
import math


inlet_from_center = 200
outlet_from_center = 200

inlet_height_from_center = 25
outlet_height_from_center = 25

radius = 100
pitch_radius = 95

gear_thickness = 40
box_thickness = 15




class Box:
    def __init__(self, x, y, z, gear_thickness, box_thickness, inlet_from_center, outlet_from_center, radius, inlet_height_from_center, outlet_height_from_center, rotX, rotZ):
        
        self.x = x
        self.y = y
        self.z = z
        self.gear_thickness = gear_thickness
        self.box_thickness = box_thickness
        self.inlet_from_center = inlet_from_center
        self.outlet_from_center = outlet_from_center
        self.radius = radius
        self.inlet_height_from_center = inlet_height_from_center
        self.outlet_height_from_center = outlet_height_from_center
        self.rotX = rotX
        #self.rotY = rotY
        self.rotZ = rotZ
        
        self.box_outline(self.x, self.y, self.z, self.gear_thickness, self.box_thickness, self.inlet_from_center, self.outlet_from_center,
                         self.radius, self.inlet_height_from_center, self.outlet_height_from_center, self.rotX, self.rotZ)
        self.box_wall(self.x, self.y, self.z, self.gear_thickness, self.box_thickness, self.inlet_from_center, self.outlet_from_center,
                      self.radius, self.inlet_height_from_center, self.outlet_height_from_center, self.rotX, self.rotZ)



    def box_outline(self, x, y, z, gear_thickness, box_thickness, inlet_from_center, outlet_from_center,
                    radius, inlet_height_from_center, outlet_height_from_center, rotX, rotZ):

        
        line_1 = Line(x, y-inlet_from_center, z+inlet_height_from_center*rotX, x, y-radius, (z+inlet_height_from_center)*rotX)
        line_2 = Line(x, y-radius, (z+inlet_height_from_center)*rotX, x, y-radius, (z+radius)*rotX)
        
        if(rotX == 1):
            arc_3  = Arc(x, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius, -90, 90)
        elif(rotX == -1):
            arc_3 = Arc(x, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius, 90, -90)
        
        line_4 = Line(x, y+radius, (z+radius)*rotX, x, y+radius, (z+outlet_height_from_center)*rotX)
        line_5 = Line(x, y+radius, (z+outlet_height_from_center)*rotX, x, y+outlet_from_center, (z+outlet_height_from_center)*rotX)

        line_6 = Line(x, y-inlet_from_center, (z+inlet_height_from_center)*rotX, x, y-inlet_from_center, (z+inlet_height_from_center+box_thickness)*rotX)
        line_7 = Line(x, y-inlet_from_center, (z+inlet_height_from_center+box_thickness)*rotX, x, y-radius-box_thickness, (z+inlet_height_from_center+box_thickness)*rotX)
        line_8 = Line(x, y-radius-box_thickness, (z+inlet_height_from_center+box_thickness)*rotX, x, y-radius-box_thickness, (z+radius)*rotX)
        
        if(rotX == 1):
            arc_9 = Arc(x, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius+box_thickness, -90, 90)
        elif(rotX == -1):
            arc_9 = Arc(x, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius+box_thickness, 90, -90)
        
        line_10 = Line(x, y+radius+box_thickness, (z+radius)*rotX, x, y+radius+box_thickness, (z+outlet_height_from_center+box_thickness)*rotX)
        line_11 = Line(x, y+radius+box_thickness, (z+outlet_height_from_center+box_thickness)*rotX, x, y+outlet_from_center, (z+outlet_height_from_center+box_thickness)*rotX)
        line_12 = Line(x, y+outlet_from_center, (z+outlet_height_from_center+box_thickness)*rotX, x, y+outlet_from_center, (z+outlet_height_from_center)*rotX)

        section = [line_1, line_2, arc_3, line_4, line_5, line_6, line_7, line_8, arc_9, line_10, line_11, line_12]

        x_line = Line(x, y, z, (x+gear_thickness/2)*rotZ, y, z)

        swept_x = Swept([x_line], section, 0, 0, 0, 0, 0)

        return swept_x


    def box_wall(self, x, y, z, gear_thickness, box_thickness, inlet_from_center, outlet_from_center,
                 radius, inlet_height_from_center, outlet_height_from_center, rotX, rotZ):

        line_1 = Line((x+gear_thickness/2)*rotZ, y-inlet_from_center, z*rotX, (x+gear_thickness/2)*rotZ, y-inlet_from_center, (z+inlet_height_from_center+box_thickness)*rotX)
        line_2 = Line((x+gear_thickness/2)*rotZ, y-inlet_from_center, (z+inlet_height_from_center+box_thickness)*rotX, (x+gear_thickness/2)*rotZ, y-radius-box_thickness, (z+inlet_height_from_center+box_thickness)*rotX)
        line_3 = Line((x+gear_thickness/2)*rotZ, y-radius-box_thickness, (z+inlet_height_from_center+box_thickness)*rotX, (x+gear_thickness/2)*rotZ, y-radius-box_thickness, (z+radius)*rotX)
        
        if(rotX == 1):
            arc_4 = Arc((x+gear_thickness/2)*rotZ, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius+box_thickness, -90, 90)
        elif(rotX == -1):
            arc_4 = Arc((x+gear_thickness/2)*rotZ, y, (z+radius)*rotX, [0, 0, 1], [0, 1, 0], radius+box_thickness, 90, -90)
        line_5 = Line((x+gear_thickness/2)*rotZ, y+radius+box_thickness, (z+radius)*rotX, (x+gear_thickness/2)*rotZ, y+radius+box_thickness, (z+outlet_height_from_center+box_thickness)*rotX)
        line_6 = Line((x+gear_thickness/2)*rotZ, y+radius+box_thickness, (z+outlet_height_from_center+box_thickness)*rotX, (x+gear_thickness/2)*rotZ, y+outlet_from_center, (z+outlet_height_from_center+box_thickness)*rotX)
        line_7 = Line((x+gear_thickness/2)*rotZ, y+outlet_from_center, (z+outlet_height_from_center+box_thickness)*rotX, (x+gear_thickness/2)*rotZ, y+outlet_from_center, z*rotX)
        line_8 = Line((x+gear_thickness/2)*rotZ, y+outlet_from_center, z*rotX, (x+gear_thickness/2)*rotZ, y-inlet_from_center, z*rotX)

        section = [line_1, line_2, line_3, arc_4, line_5, line_6, line_7, line_8]

        x_line = Line((x+gear_thickness/2)*rotZ, y, z, (x+gear_thickness/2+box_thickness)*rotZ, y, z)

        swept_x = Swept([x_line], section, 0, 0, 0, 0, 0)

        return swept_x




def main():
    
    upper_box_1 = Box(0, 0, 0, gear_thickness, box_thickness, inlet_from_center, outlet_from_center, radius, inlet_height_from_center, outlet_height_from_center, 1, 1)
    upper_box_2 = Box(0, 0, 0, gear_thickness, box_thickness, inlet_from_center, outlet_from_center, radius, inlet_height_from_center, outlet_height_from_center, 1, -1)

    under_box_1 = Box(0, 0, 0, gear_thickness, box_thickness, inlet_from_center, outlet_from_center, radius, inlet_height_from_center, outlet_height_from_center, -1, 1)
    under_box_2 = Box(0, 0, 0, gear_thickness, box_thickness, inlet_from_center, outlet_from_center, radius, inlet_height_from_center, outlet_height_from_center, -1, -1)
main()