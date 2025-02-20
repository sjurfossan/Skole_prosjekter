import NXOpen

class Save:
    def __init__(self, folder, filename):
        self.folder = folder
        self.fileName = filename
        
        theSession  = NXOpen.Session.GetSession()
        self.theSession  = theSession
        self.workPart = theSession.Parts.Work
        self.displayPart = theSession.Parts.Display
        
        self.initForNX()
        
    def initForNX(self):
		#Getting 'fileName' to provide a proper reference to the model.
		#Made based on Save As... journal
        pathToTheFolder = self.folder
        fileName = self.fileName
        #Basic references
        theSession  = self.theSession 
        workPart = self.workPart
        displayPart = self.displayPart
		#Saving prt file, so now we will know and have a control over the name of the model.
        partSaveStatus1 = workPart.SaveAs(pathToTheFolder + fileName + ".prt")
        partSaveStatus1.Dispose()