from Shapes.Arc import Arc
from Shapes.Line import Line
from Shapes.Swept import Swept

class Spout:

    def __init__(self, x, y, z, radius, radius_spout):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.radius_spoout = radius_spout

        self.spout_swept(self.x, self.y, self.z, self.radius, self.radius_spoout)
    
    def spout_swept(self, x, y, z, radius, radius_spout):
        path_line_1 = Line(x, y, z, x, y-radius/7, z)
        path_line_2 = Arc(x, y-radius/7, z+radius/2.5, [0, 0, 1], [0, 1, 0], radius/2.5, 180, 270)
        path_line_3 = Arc(x, y-2*radius/2.5-radius/7, z+radius/2.5, [0, 0, -1], [0, 1, 0], radius/2.5, 90, 180)
        spout_guide = [path_line_1, path_line_2, path_line_3]

        #INNSIDE-RADIUS TIL SPOUT ER RADIUS/12
        spout_sketch_outline = Arc(x, y, z, [0, 0, 1], [1, 0, 0], radius_spout, 0, 360)
        spout_sketch_inside = Arc(x, y, z, [0, 0, 1], [1, 0, 0], radius_spout/1.2, 0, 360)

        swept_body_outline = Swept(spout_guide, [spout_sketch_outline])
        swept_body_inside = Swept(spout_guide, [spout_sketch_inside])
        swept_body_outline.subtract(swept_body_inside)

        spout_sketch_end_line_1 = Line(x+radius/2, y-2*radius/2.5-radius/5, z+radius/2.5, x+radius/2, y-2*radius/2.5, z+radius)
        spout_sketch_end_line_2 = Line(x+radius/2, y-2*radius/2.5, z+radius, x+radius/2, y-2*radius, z+radius)
        spout_sketch_end_line_3 = Line(x+radius/2, y-2*radius, z+radius, x+radius/2, y-2*radius/2.5-radius/5, z+radius/2.5)
        swept_end_subtract = Swept([Line(x+radius*2, y-2*radius-radius/7, z+radius*1.2, x-radius*2, y-2*radius-radius/7, z+radius*1.2)],
                                   [spout_sketch_end_line_1, spout_sketch_end_line_2, spout_sketch_end_line_3])
        swept_body_outline.subtract(swept_end_subtract)
        
