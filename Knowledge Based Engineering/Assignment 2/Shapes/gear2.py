import math
from Line import Line


class GearShape:
    def __init__(self, dia, height, teeth):
        self.dia = dia
        self.height = height
        self.teeth = teeth

        self.lines = []

        # Create the lines for the gear body.
        for i in range(teeth):
            angle = (2 * math.pi * i) / teeth
            x0 = dia / 2 * math.cos(angle)
            y0 = dia / 2 * math.sin(angle)
            x1 = dia / 2 * math.cos(angle + math.pi)
            y1 = dia / 2 * math.sin(angle + math.pi)

            self.lines.append(Line(x0, y0, 0, x1, y1, 0))

        # Create the lines for the gear teeth.
        for i in range(teeth):
            angle = (2 * math.pi * i) / teeth
            x0 = dia / 4 * math.cos(angle)
            y0 = dia / 4 * math.sin(angle)
            x1 = dia / 2 * math.cos(angle)
            y1 = dia / 2 * math.sin(angle)
            x2 = dia / 2 * math.cos(angle + math.pi / 2)
            y2 = dia / 2 * math.sin(angle + math.pi / 2)
            x3 = dia / 4 * math.cos(angle + math.pi)
            y3 = dia / 4 * math.sin(angle + math.pi)

            self.lines.append(Line(x0, y0, 0, x1, y1, 0))
            self.lines.append(Line(x1, y1, 0, x2, y2, 0))
            self.lines.append(Line(x2, y2, 0, x3, y3, 0))
            self.lines.append(Line(x3, y3, 0, x0, y0, 0))

    def get_lines(self):
        return self.lines

def main():
    dia = 100
    height = 10
    teeth = 10

    gear_shape = GearShape(dia, height, teeth)
    lines = gear_shape.get_lines()

    # Save the lines to a file.
    with open("gear_shape.lines", "w") as f:
        for line in lines:
            f.write(f"{line.x0} {line.y0} {line.z0} {line.x1} {line.y1} {line.z1}\n")

if __name__ == "__main__":
    main()