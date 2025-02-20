from Shapes.Arc import Arc
from Shapes.Swept import Swept
from Shapes.Line import Line
from Shapes.Sphere import Sphere
from Shapes.Cylinder import Cylinder
from Shapes.Cone import Cone
from GA.ga_volume import GeneticAlgorithmVolume
from math import sqrt as sqrt
from math import cos as cos
from math import sin as sin
from math import tan as tan
from math import radians as radians


class Teapot_body:
    def __init__(self, radius, radius_spout):
        self.radius = radius
        self.radius_spout = radius_spout

        self.teapot_body(self.radius, self.radius_spout)

    def teapot_body(self, radius, radius_spout):
        teapot_body_outline = Sphere(0, 0, 0, radius*2)
        teapot_body_inside = Sphere(0, 0, 0, radius*1.90)


        teapot_body_bottom = Cylinder(0, 0, -radius*0.87, 2*sqrt(radius**2-(radius*0.8)**2), radius*0.07)

        teapot_lid_cylinder = Cylinder(0, 0, radius*0.8, 2*sqrt(radius**2-(radius*0.8)**2), radius*0.07)
        teapot_lid_cone = Cone(0, 0, radius*0.8+radius*0.07, 2*sqrt(radius**2-(radius*0.8)**2), sqrt(radius**2-(radius*0.8)**2), radius/6)
        teapot_lid_sphere = Sphere(0, 0, radius*0.8+radius*0.07+radius/4.7, sqrt(radius**2-(radius*0.8)**2)/3)

        subtract_cyl_1 = Cylinder(0, 0, radius*0.80, radius*2, radius)
        subtract_cyl_2 = Cylinder(0, 0, -radius*2, radius*2, (radius*1.2))
        
        teapot_body_outline.subtract(teapot_body_inside)
        teapot_body_outline.subtract(subtract_cyl_1)
        teapot_body_outline.subtract(subtract_cyl_2)

        teapot_handle_sketch = Arc(0, sqrt(radius**2-(radius*0.7)**2)-radius*0.055, radius*0.7, [0, 0, 1], [1, 0, 0], radius*0.05, 0, 360)
        teapot_handle_guide_line_1 = Line(0, sqrt(radius**2-(radius*0.7)**2)-radius*0.055, radius*0.7, 0, sqrt(radius**2-(radius*0.7)**2)+radius*0.3, radius*0.7)
        teapot_handle_guide_line_2 = Arc(0, sqrt(radius**2-(radius*0.7)**2)+radius*0.3, radius*0.5, [0, 0, 1], [0, 1, 0], radius*0.2, 0, 90)
        teapot_handle_guide_line_3 = Line(0, sqrt(radius**2-(radius*0.7)**2)+radius*0.5, radius*0.5, 0, sqrt(radius**2-(radius*0.7)**2)+radius*0.5, -radius*0.4)
        teapot_handle_guide = [teapot_handle_guide_line_1, teapot_handle_guide_line_2, teapot_handle_guide_line_3]
        teapot_handle_swept = Swept(teapot_handle_guide, [teapot_handle_sketch])
        teapot_handle_end_line_1 = Line(radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.3, -radius*0.4, radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.7, radius*0.2)
        teapot_handle_end_line_2 = Line(radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.7, radius*0.2, radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.9, -radius*0.4)
        teapot_handle_end_line_3 = Line(radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.9, -radius*0.4, radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.3, -radius*0.4)
        teapot_handle_end_swept_subtract = Swept([Line(radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.5, -radius*0.4, -radius*0.5, sqrt(radius**2-(radius*0.7)**2)+radius*0.5, -radius*0.4)],
                                                [teapot_handle_end_line_1, teapot_handle_end_line_2, teapot_handle_end_line_3])
        teapot_handle_swept.subtract(teapot_handle_end_swept_subtract)


        #DETTE ER STARTPOSISJONEN TIL SPOUT!!
        spout_hole_sketch = Arc(0, -radius*0.8, -radius*0.3, [0, 0, 1], [1, 0, 0], radius_spout, 0, 360)
        spout_hole_swept_subtract = Swept([Line(0, -radius*0.8, -radius*0.3, 0, -radius*2, -radius*0.3)], [spout_hole_sketch])
        teapot_body_outline.subtract(spout_hole_swept_subtract)

"""
radius = 30
teapot_1 = Teapot_body(radius)
"""
"""
def main():
    try:
        target_flow = 30
        population_size = 10
        mutation_rate = 0.15

        ga = GeneticAlgorithmVolume(target_flow, population_size, mutation_rate)
        bod = Teapot_body(0, 0, 0, ga.best_radius)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the target flow.")

if __name__ == "__main__":
    main()"""