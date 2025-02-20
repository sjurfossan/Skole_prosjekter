import math
import NXOpen

class FileSaver:

	def __init__(self, filePath, fileName):
		
		self.filePath = filePath
		self.fileName = fileName

		self.initForNX()

	def initForNX(self):
		theSession = NXOpen.Session.GetSession()
		workPart = theSession.Parts.Work

		partSaveStatus1 = workPart.SaveAs(self.filePath + self.fileName + ".prt")
		partSaveStatus1.Dispose()


