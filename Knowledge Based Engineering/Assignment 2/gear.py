from Shapes.Cylinder import Cylinder
import math as m


class Gear:
	def __init__(self, mod, disk_dia, disk_height, const, y_diff):
		
		#self.x = x
		#self.y = y
		#self.z = z
		self.mod = mod
		self.const = const
		self.disk_dia = disk_dia
		self.disk_height = disk_height
		self.teeth_amt = int(disk_dia*mod)
		self.angle = 2*m.pi/self.teeth_amt
		self.tooth_dia = m.pi*self.disk_dia/(2*self.teeth_amt)
		self.angleRotate = self.const*self.angle/2
		
		self.y_diff = y_diff


		#self.gear_body(self.mod, self.disk_dia, self.disk_height, self.const, self.y_diff,
		#		 self.teeth_amt, self.angle, self.angleRotate, self.tooth_dia)
		

	#def gear_body(self, mod, disk_dia, disk_height, const, y_diff, teeth_amt, angle, angleRotate, tooth_dia):
		buttonDisk = Cylinder(0, 0, 0, disk_dia, disk_height)
		pole = Cylinder(0, 0, disk_height/5, disk_dia/3, disk_height*1.8)
		
		buttonDisk.unite(pole)


		for i in range(0, self.teeth_amt):
			
			x = disk_dia/2*m.cos(i*self.angle + self.angleRotate)
			y = disk_dia/2*m.sin(i*self.angle + self.angleRotate) + y_diff

			cyl = Cylinder(x, y, 0, self.tooth_dia, disk_height)
			
			buttonDisk.subtract(cyl)

		for i in range(0, self.teeth_amt):

			x = disk_dia/2*m.cos(i*self.angle + self.angle/2 + self.angleRotate)
			y = disk_dia/2*m.sin(i*self.angle + self.angle/2 + self.angleRotate) + y_diff

			cyl = Cylinder(x, y, 0, self.tooth_dia, disk_height)		
			
			buttonDisk.unite(cyl)

				
gear_1 = Gear(0.7, 20, 5, 0, 0)
#gear_2 = Gear(20, 20, 20, 0.7, 20, 5, 0, 0)
