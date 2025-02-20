import random
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Motion

class Motion3:
	def __init__(self, fileName, filePath):	
		self.fileName = fileName
		self.filePath = filePath
		self.initForNX()

	def initForNX(self):
		theSession  = NXOpen.Session.GetSession()
		workPart = theSession.Parts.Work
		displayPart = theSession.Parts.Display
		# ----------------------------------------------
		#   Menu: Application->Simulation->Motion
		# ----------------------------------------------
		markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Motion")
		
		theSession.ApplicationSwitchImmediate("UG_APP_MECHANISMS")
		
		globalSelectionBuilder1 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: File->Utilities->New Simulation...
		# ----------------------------------------------
		markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		fileNew1 = theSession.Parts.FileNew()
		
		theSession.SetUndoMarkName(markId2, "New Simulation Dialog")
		
		markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
		
		theSession.DeleteUndoMark(markId3, None)
		
		markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
		
		fileNew1.TemplateFileName = "Simcenter 3D Motion"
		
		fileNew1.UseBlankTemplate = True
		
		fileNew1.ApplicationName = "MotionTemplate"
		
		fileNew1.Units = NXOpen.Part.Units.Millimeters
		
		fileNew1.RelationType = ""
		
		fileNew1.UsesMasterModel = "Yes"
		
		fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
		
		fileNew1.TemplatePresentationName = ""
		
		fileNew1.ItemType = ""
		
		fileNew1.Specialization = ""
		
		fileNew1.SetCanCreateAltrep(False)
		
		fileNew1.NewFileName = self.filePath + str(random.randrange(1,1000))+".sim" 
		
		fileNew1.MasterFileName = self.fileName
		
		fileNew1.MakeDisplayedPart = True
		
		fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
		
		theSession.DeleteUndoMark(markId4, None)
		
		theSession.SetUndoMarkName(markId2, "New Simulation")
		
		baseTemplateManager2 = theSession.XYPlotManager.TemplateManager
		
		nXObject1 = fileNew1.Commit()
		
		workPart = theSession.Parts.Work # Gear284_motion1
		displayPart = theSession.Parts.Display # Gear284_motion1
		markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
		
		theSession.SetUndoMarkName(markId5, "Environment Dialog")
		
		# ----------------------------------------------
		#   Dialog Begin Environment
		# ----------------------------------------------
		markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Environment")
		
		theSession.DeleteUndoMark(markId6, None)
		
		markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Environment")
		
		theSession.MotionSession.Environments.SetAnalysisType(NXOpen.Motion.MotionEnvironment.Analysis.Dynamics)
		
		theSession.MotionSession.Environments.SetComponentBasedMechanism(False)
		
		theSession.MotionSession.Environments.SetJointWizardStatus(NXOpen.Motion.MotionEnvironment.JointWizardStatus.On)
		
		nErrs1 = theSession.UpdateManager.DoUpdate(markId5)
		
		theSession.DeleteUndoMark(markId7, None)
		
		theSession.SetUndoMarkName(markId5, "Environment")
		
		theSession.DeleteUndoMark(markId5, None)
		
		theSession.MotionSession.InitializeSimulation(workPart)
		
		physicsConversionBuilder1 = theSession.MotionSession.CreatePhysicsConversionBuilder(workPart)
		
		animationConversionBuilder1 = theSession.MotionSession.CreateAnimationConversionBuilder(workPart)
		
		physicsConversionBuilder1.Destroy()
		
		animationConversionBuilder1.Destroy()
		
		theSession.MotionSession.MotionMethods.ModelCheck(False)
		
		fileNew1.Destroy()

		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Insert->Motion Body...
		# ----------------------------------------------
		markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		linkBuilder1 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
		
		linkBuilder1.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
		
		linkBuilder1.MassProperty.MassExpression.SetFormula("1")
		
		linkBuilder1.MassProperty.IxxExpression.SetFormula("1")
		
		linkBuilder1.MassProperty.IyyExpression.SetFormula("1")
		
		linkBuilder1.MassProperty.IzzExpression.SetFormula("1")
		
		linkBuilder1.MassProperty.IxyExpression.SetFormula("0")
		
		linkBuilder1.MassProperty.IxzExpression.SetFormula("0")
		
		linkBuilder1.MassProperty.IyzExpression.SetFormula("0")
		
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoMassExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIxxExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIyyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIzzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIxyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIxzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder1.MassProperty.AutoIyzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		linkBuilder1.InitialVelocity.TranslateExpression.SetFormula("0")
		
		linkBuilder1.InitialVelocity.RotateExpression.SetFormula("0")
		
		linkBuilder1.InitialVelocity.WxExpression.SetFormula("0")
		
		linkBuilder1.InitialVelocity.WyExpression.SetFormula("0")
		
		linkBuilder1.InitialVelocity.WzExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId8, "Motion Body Dialog")
		
		unit1 = workPart.UnitCollection.FindObject("MilliMeter")
		expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		globalSelectionBuilder2 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList1 = globalSelectionBuilder2.Selection
		
		component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT "+self.fileName + " 1")
		body1 = component1.FindObject("PROTO#.Bodies|CYLINDER(1)")
		added1 = linkBuilder1.Geometries.Add(body1)
		
		globalSelectionBuilder3 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList2 = globalSelectionBuilder3.Selection
		
		markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
		
		linkBuilder1.InitialVelocity.TranslateVector = NXOpen.Direction.Null
		
		linkBuilder1.InitialVelocity.RotateVector = NXOpen.Direction.Null
		
		nXObject2 = linkBuilder1.Commit()
		
		theSession.DeleteUndoMark(markId9, None)
		
		theSession.SetUndoMarkName(markId8, "Motion Body")
		
		linkBuilder1.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression1)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression2)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		linkBuilder2 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
		
		linkBuilder2.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
		
		linkBuilder2.MassProperty.MassExpression.SetFormula("1")
		
		linkBuilder2.MassProperty.IxxExpression.SetFormula("1")
		
		linkBuilder2.MassProperty.IyyExpression.SetFormula("1")
		
		linkBuilder2.MassProperty.IzzExpression.SetFormula("1")
		
		linkBuilder2.MassProperty.IxyExpression.SetFormula("0")
		
		linkBuilder2.MassProperty.IxzExpression.SetFormula("0")
		
		linkBuilder2.MassProperty.IyzExpression.SetFormula("0")
		
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoMassExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIxxExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIyyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIzzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIxyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIxzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder2.MassProperty.AutoIyzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		linkBuilder2.InitialVelocity.TranslateExpression.SetFormula("0")
		
		linkBuilder2.InitialVelocity.RotateExpression.SetFormula("0")
		
		linkBuilder2.InitialVelocity.WxExpression.SetFormula("0")
		
		linkBuilder2.InitialVelocity.WyExpression.SetFormula("0")
		
		linkBuilder2.InitialVelocity.WzExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId10, "Motion Body Dialog")
		
		expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		# ----------------------------------------------
		#   Dialog Begin Motion Body
		# ----------------------------------------------
		globalSelectionBuilder4 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList3 = globalSelectionBuilder4.Selection
		
		body2 = component1.FindObject("PROTO#.Bodies|CYLINDER(60)")
		added2 = linkBuilder2.Geometries.Add(body2)
		
		globalSelectionBuilder5 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList4 = globalSelectionBuilder5.Selection
		
		markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
		
		linkBuilder2.InitialVelocity.TranslateVector = NXOpen.Direction.Null
		
		linkBuilder2.InitialVelocity.RotateVector = NXOpen.Direction.Null
		
		nXObject3 = linkBuilder2.Commit()
		
		theSession.DeleteUndoMark(markId11, None)
		
		theSession.SetUndoMarkName(markId10, "Motion Body")
		
		linkBuilder2.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression3)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression4)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		linkBuilder3 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
		
		linkBuilder3.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
		
		linkBuilder3.MassProperty.MassExpression.SetFormula("1")
		
		linkBuilder3.MassProperty.IxxExpression.SetFormula("1")
		
		linkBuilder3.MassProperty.IyyExpression.SetFormula("1")
		
		linkBuilder3.MassProperty.IzzExpression.SetFormula("1")
		
		linkBuilder3.MassProperty.IxyExpression.SetFormula("0")
		
		linkBuilder3.MassProperty.IxzExpression.SetFormula("0")
		
		linkBuilder3.MassProperty.IyzExpression.SetFormula("0")
		
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoMassExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIxxExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIyyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIzzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIxyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIxzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder3.MassProperty.AutoIyzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		linkBuilder3.InitialVelocity.TranslateExpression.SetFormula("0")
		
		linkBuilder3.InitialVelocity.RotateExpression.SetFormula("0")
		
		linkBuilder3.InitialVelocity.WxExpression.SetFormula("0")
		
		linkBuilder3.InitialVelocity.WyExpression.SetFormula("0")
		
		linkBuilder3.InitialVelocity.WzExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId12, "Motion Body Dialog")
		
		expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		# ----------------------------------------------
		#   Dialog Begin Motion Body
		# ----------------------------------------------
		globalSelectionBuilder6 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList5 = globalSelectionBuilder6.Selection
		
		body3 = component1.FindObject("PROTO#.Bodies|CYLINDER(119)")
		added3 = linkBuilder3.Geometries.Add(body3)
		
		globalSelectionBuilder7 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList6 = globalSelectionBuilder7.Selection
		
		markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
		
		linkBuilder3.InitialVelocity.TranslateVector = NXOpen.Direction.Null
		
		linkBuilder3.InitialVelocity.RotateVector = NXOpen.Direction.Null
		
		nXObject4 = linkBuilder3.Commit()
		
		theSession.DeleteUndoMark(markId13, None)
		
		theSession.SetUndoMarkName(markId12, "Motion Body")
		
		linkBuilder3.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression5)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression6)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		linkBuilder4 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
		
		linkBuilder4.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
		
		linkBuilder4.MassProperty.MassExpression.SetFormula("1")
		
		linkBuilder4.MassProperty.IxxExpression.SetFormula("1")
		
		linkBuilder4.MassProperty.IyyExpression.SetFormula("1")
		
		linkBuilder4.MassProperty.IzzExpression.SetFormula("1")
		
		linkBuilder4.MassProperty.IxyExpression.SetFormula("0")
		
		linkBuilder4.MassProperty.IxzExpression.SetFormula("0")
		
		linkBuilder4.MassProperty.IyzExpression.SetFormula("0")
		
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoMassExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIxxExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIyyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIzzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIxyExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIxzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		try:
			# This expression cannot be modified because it is locked.
			linkBuilder4.MassProperty.AutoIyzExpression.SetFormula("0")
		except NXOpen.NXException as ex:
			ex.AssertErrorCode(1050049)
			
		linkBuilder4.InitialVelocity.TranslateExpression.SetFormula("0")
		
		linkBuilder4.InitialVelocity.RotateExpression.SetFormula("0")
		
		linkBuilder4.InitialVelocity.WxExpression.SetFormula("0")
		
		linkBuilder4.InitialVelocity.WyExpression.SetFormula("0")
		
		linkBuilder4.InitialVelocity.WzExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId14, "Motion Body Dialog")
		
		expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		# ----------------------------------------------
		#   Dialog Begin Motion Body
		# ----------------------------------------------
		globalSelectionBuilder8 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList7 = globalSelectionBuilder8.Selection
		
		body4 = component1.FindObject("PROTO#.Bodies|CYLINDER(178)")
		added4 = linkBuilder4.Geometries.Add(body4)
		
		markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
		
		globalSelectionBuilder9 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList8 = globalSelectionBuilder9.Selection
		
		theSession.DeleteUndoMark(markId15, None)
		
		markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
		
		linkBuilder4.InitialVelocity.TranslateVector = NXOpen.Direction.Null
		
		linkBuilder4.InitialVelocity.RotateVector = NXOpen.Direction.Null
		
		nXObject5 = linkBuilder4.Commit()
		
		theSession.DeleteUndoMark(markId16, None)
		
		theSession.SetUndoMarkName(markId14, "Motion Body")
		
		linkBuilder4.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression7)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression8)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Insert->Joint...
		# ----------------------------------------------
		markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		jointBuilder1 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
		
		jointBuilder1.JointDefine.UpperLimitExpression.SetFormula("0")
		
		jointBuilder1.JointDefine.LowerLimitExpression.SetFormula("0")
		
		jointBuilder1.JointDefine.UpperLimitAngleExpression.SetFormula("0")
		
		jointBuilder1.JointDefine.LowerLimitAngleExpression.SetFormula("0")
		
		jointBuilder1.JointDefine.ScrewRatioExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder1.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder1.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder1.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder1.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder1.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder1.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder1.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder1.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
		
		jointBuilder1.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder1.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
		
		jointBuilder1.JointFriction.LmsFriction.MuStatic.SetFormula("0")
		
		jointBuilder1.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
		
		jointBuilder1.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
		
		jointBuilder1.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
		
		jointBuilder1.JointFriction.LmsFriction.PinRadius.SetFormula("1")
		
		jointBuilder1.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
		
		jointBuilder1.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
		
		jointBuilder1.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
		
		jointBuilder1.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
		
		jointBuilder1.JointFriction.LmsFriction.BallRadius.SetFormula("1")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId17, "Joint Dialog")
		
		expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		jointBuilder1.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
		
		jointBuilder1.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		globalSelectionBuilder10 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList9 = globalSelectionBuilder10.Selection
		
		globalSelectionBuilder11 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList10 = globalSelectionBuilder11.Selection
		
		globalSelectionBuilder12 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList11 = globalSelectionBuilder12.Selection
		
		link1 = nXObject2
		jointBuilder1.JointDefine.FirstLinkSelection.Value = link1
		
		globalSelectionBuilder13 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList12 = globalSelectionBuilder13.Selection
		
		expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		part1 = theSession.Parts.FindObject(self.fileName)
		cylinder1 = part1.Features.FindObject("CYLINDER(2)")
		edge1 = cylinder1.FindObject("EDGE * 1 * 3 {(-0.5,-0.8660254037844,10)(1,0,10)(-0.5,0.8660254037844,10) CYLINDER(1)}")
		point1 = workPart.Points.CreatePoint(edge1, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		edge2 = component1.FindObject("PROTO#.Features|CYLINDER(2)|EDGE * 1 * 3 {(-0.5,-0.8660254037844,10)(1,0,10)(-0.5,0.8660254037844,10) CYLINDER(1)}")
		xform1, nXObject6 = workPart.Xforms.CreateExtractXform(edge2, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point2 = workPart.Points.CreatePoint(point1, xform1, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		globalSelectionBuilder14 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList13 = globalSelectionBuilder14.Selection
		
		partLoadStatus1 = part1.LoadFeatureDataForSelection()
		
		partLoadStatus1.Dispose()
		edge3 = nXObject6
		point3 = workPart.Points.CreatePoint(edge3, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		xform2, nXObject7 = workPart.Xforms.CreateExtractXform(edge2, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point4 = workPart.Points.CreatePoint(point3, xform2, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder1.JointDefine.FirstOrigin = point4
		
		origin1 = NXOpen.Point3d(0.0, 0.0, 10.000000000000002)
		xDirection1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
		yDirection1 = NXOpen.Vector3d(0.0, 1.0, 0.0)
		xform3 = workPart.Xforms.CreateXform(origin1, xDirection1, yDirection1, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
		
		cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder1.JointDefine.FirstCsys = cartesianCoordinateSystem1
		
		globalSelectionBuilder15 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList14 = globalSelectionBuilder15.Selection
		
		globalSelectionBuilder16 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList15 = globalSelectionBuilder16.Selection
		
		globalSelectionBuilder17 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList16 = globalSelectionBuilder17.Selection
		
		origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
		vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
		direction1 = workPart.Directions.CreateDirection(origin2, vector1, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder1.JointDefine.FirstVector = direction1
		
		markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
		
		nXObject8 = jointBuilder1.Commit()
		
		theSession.DeleteUndoMark(markId18, None)
		
		theSession.SetUndoMarkName(markId17, "Joint")
		
		jointBuilder1.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression15)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.Points.DeletePoint(point2)
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression9)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression10)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression11)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression12)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression13)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression14)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		jointBuilder2 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
		
		jointBuilder2.JointDefine.UpperLimitExpression.SetFormula("0")
		
		jointBuilder2.JointDefine.LowerLimitExpression.SetFormula("0")
		
		jointBuilder2.JointDefine.UpperLimitAngleExpression.SetFormula("0")
		
		jointBuilder2.JointDefine.LowerLimitAngleExpression.SetFormula("0")
		
		jointBuilder2.JointDefine.ScrewRatioExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder2.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder2.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder2.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder2.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder2.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder2.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder2.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder2.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
		
		jointBuilder2.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder2.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
		
		jointBuilder2.JointFriction.LmsFriction.MuStatic.SetFormula("0")
		
		jointBuilder2.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
		
		jointBuilder2.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
		
		jointBuilder2.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
		
		jointBuilder2.JointFriction.LmsFriction.PinRadius.SetFormula("1")
		
		jointBuilder2.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
		
		jointBuilder2.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
		
		jointBuilder2.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
		
		jointBuilder2.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
		
		jointBuilder2.JointFriction.LmsFriction.BallRadius.SetFormula("1")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId19, "Joint Dialog")
		
		expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		jointBuilder2.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
		
		jointBuilder2.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		# ----------------------------------------------
		#   Dialog Begin Joint
		# ----------------------------------------------
		globalSelectionBuilder18 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList17 = globalSelectionBuilder18.Selection
		
		globalSelectionBuilder19 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList18 = globalSelectionBuilder19.Selection
		
		globalSelectionBuilder20 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList19 = globalSelectionBuilder20.Selection
		
		link2 = nXObject3
		jointBuilder2.JointDefine.FirstLinkSelection.Value = link2
		
		globalSelectionBuilder21 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList20 = globalSelectionBuilder21.Selection
		
		expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		cylinder2 = part1.Features.FindObject("CYLINDER(61)")
		edge4 = cylinder2.FindObject("EDGE * 1 * 3 {(-0.5,19.1339745962156,10)(1,20,10)(-0.5,20.8660254037844,10) CYLINDER(60)}")
		point5 = workPart.Points.CreatePoint(edge4, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		edge5 = component1.FindObject("PROTO#.Features|CYLINDER(61)|EDGE * 1 * 3 {(-0.5,19.1339745962156,10)(1,20,10)(-0.5,20.8660254037844,10) CYLINDER(60)}")
		xform4, nXObject9 = workPart.Xforms.CreateExtractXform(edge5, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point6 = workPart.Points.CreatePoint(point5, xform4, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		globalSelectionBuilder22 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList21 = globalSelectionBuilder22.Selection
		
		partLoadStatus2 = part1.LoadFeatureDataForSelection()
		
		partLoadStatus2.Dispose()
		edge6 = nXObject9
		point7 = workPart.Points.CreatePoint(edge6, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		xform5, nXObject10 = workPart.Xforms.CreateExtractXform(edge5, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point8 = workPart.Points.CreatePoint(point7, xform5, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder2.JointDefine.FirstOrigin = point8
		
		origin3 = NXOpen.Point3d(0.0, 20.0, 10.000000000000002)
		xDirection2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
		yDirection2 = NXOpen.Vector3d(0.0, 1.0, 0.0)
		xform6 = workPart.Xforms.CreateXform(origin3, xDirection2, yDirection2, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
		
		cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform6, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder2.JointDefine.FirstCsys = cartesianCoordinateSystem2
		
		globalSelectionBuilder23 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList22 = globalSelectionBuilder23.Selection
		
		globalSelectionBuilder24 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList23 = globalSelectionBuilder24.Selection
		
		globalSelectionBuilder25 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList24 = globalSelectionBuilder25.Selection
		
		origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
		vector2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
		direction2 = workPart.Directions.CreateDirection(origin4, vector2, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder2.JointDefine.FirstVector = direction2
		
		markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
		
		nXObject11 = jointBuilder2.Commit()
		
		theSession.DeleteUndoMark(markId20, None)
		
		theSession.SetUndoMarkName(markId19, "Joint")
		
		jointBuilder2.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression22)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.Points.DeletePoint(point6)
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression16)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression17)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression18)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression19)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression20)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression21)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		jointBuilder3 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
		
		jointBuilder3.JointDefine.UpperLimitExpression.SetFormula("0")
		
		jointBuilder3.JointDefine.LowerLimitExpression.SetFormula("0")
		
		jointBuilder3.JointDefine.UpperLimitAngleExpression.SetFormula("0")
		
		jointBuilder3.JointDefine.LowerLimitAngleExpression.SetFormula("0")
		
		jointBuilder3.JointDefine.ScrewRatioExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder3.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder3.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder3.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder3.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder3.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder3.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder3.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder3.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
		
		jointBuilder3.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder3.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
		
		jointBuilder3.JointFriction.LmsFriction.MuStatic.SetFormula("0")
		
		jointBuilder3.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
		
		jointBuilder3.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
		
		jointBuilder3.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
		
		jointBuilder3.JointFriction.LmsFriction.PinRadius.SetFormula("1")
		
		jointBuilder3.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
		
		jointBuilder3.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
		
		jointBuilder3.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
		
		jointBuilder3.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
		
		jointBuilder3.JointFriction.LmsFriction.BallRadius.SetFormula("1")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId21, "Joint Dialog")
		
		expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		jointBuilder3.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
		
		jointBuilder3.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder3.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		# ----------------------------------------------
		#   Dialog Begin Joint
		# ----------------------------------------------
		globalSelectionBuilder26 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList25 = globalSelectionBuilder26.Selection
		
		globalSelectionBuilder27 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList26 = globalSelectionBuilder27.Selection
		
		globalSelectionBuilder28 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList27 = globalSelectionBuilder28.Selection
		
		link3 = nXObject4
		jointBuilder3.JointDefine.FirstLinkSelection.Value = link3
		
		globalSelectionBuilder29 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList28 = globalSelectionBuilder29.Selection
		
		expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		cylinder3 = part1.Features.FindObject("CYLINDER(120)")
		edge7 = cylinder3.FindObject("EDGE * 1 * 3 {(-0.5,39.1339745962156,10)(1,40,10)(-0.5,40.8660254037844,10) CYLINDER(119)}")
		point9 = workPart.Points.CreatePoint(edge7, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		edge8 = component1.FindObject("PROTO#.Features|CYLINDER(120)|EDGE * 1 * 3 {(-0.5,39.1339745962156,10)(1,40,10)(-0.5,40.8660254037844,10) CYLINDER(119)}")
		xform7, nXObject12 = workPart.Xforms.CreateExtractXform(edge8, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point10 = workPart.Points.CreatePoint(point9, xform7, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		globalSelectionBuilder30 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList29 = globalSelectionBuilder30.Selection
		
		partLoadStatus3 = part1.LoadFeatureDataForSelection()
		
		partLoadStatus3.Dispose()
		edge9 = nXObject12
		point11 = workPart.Points.CreatePoint(edge9, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		xform8, nXObject13 = workPart.Xforms.CreateExtractXform(edge8, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point12 = workPart.Points.CreatePoint(point11, xform8, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder3.JointDefine.FirstOrigin = point12
		
		origin5 = NXOpen.Point3d(0.0, 40.0, 10.000000000000002)
		xDirection3 = NXOpen.Vector3d(1.0, 0.0, 0.0)
		yDirection3 = NXOpen.Vector3d(0.0, 1.0, 0.0)
		xform9 = workPart.Xforms.CreateXform(origin5, xDirection3, yDirection3, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
		
		cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform9, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder3.JointDefine.FirstCsys = cartesianCoordinateSystem3
		
		globalSelectionBuilder31 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList30 = globalSelectionBuilder31.Selection
		
		globalSelectionBuilder32 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList31 = globalSelectionBuilder32.Selection
		
		globalSelectionBuilder33 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList32 = globalSelectionBuilder33.Selection
		
		origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
		vector3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
		direction3 = workPart.Directions.CreateDirection(origin6, vector3, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder3.JointDefine.FirstVector = direction3
		
		markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
		
		nXObject14 = jointBuilder3.Commit()
		
		theSession.DeleteUndoMark(markId22, None)
		
		theSession.SetUndoMarkName(markId21, "Joint")
		
		jointBuilder3.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression29)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.Points.DeletePoint(point10)
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression23)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression24)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression25)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression26)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression27)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression28)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		jointBuilder4 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
		
		jointBuilder4.JointDefine.UpperLimitExpression.SetFormula("0")
		
		jointBuilder4.JointDefine.LowerLimitExpression.SetFormula("0")
		
		jointBuilder4.JointDefine.UpperLimitAngleExpression.SetFormula("0")
		
		jointBuilder4.JointDefine.LowerLimitAngleExpression.SetFormula("0")
		
		jointBuilder4.JointDefine.ScrewRatioExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder4.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder4.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder4.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder4.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
		
		jointBuilder4.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
		
		jointBuilder4.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
		
		jointBuilder4.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
		
		jointBuilder4.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
		
		jointBuilder4.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
		
		jointBuilder4.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
		
		jointBuilder4.JointFriction.LmsFriction.MuStatic.SetFormula("0")
		
		jointBuilder4.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
		
		jointBuilder4.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
		
		jointBuilder4.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
		
		jointBuilder4.JointFriction.LmsFriction.PinRadius.SetFormula("1")
		
		jointBuilder4.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
		
		jointBuilder4.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
		
		jointBuilder4.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
		
		jointBuilder4.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
		
		jointBuilder4.JointFriction.LmsFriction.BallRadius.SetFormula("1")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId23, "Joint Dialog")
		
		expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		jointBuilder4.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
		
		jointBuilder4.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointBuilder4.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		# ----------------------------------------------
		#   Dialog Begin Joint
		# ----------------------------------------------
		globalSelectionBuilder34 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList33 = globalSelectionBuilder34.Selection
		
		globalSelectionBuilder35 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList34 = globalSelectionBuilder35.Selection
		
		globalSelectionBuilder36 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList35 = globalSelectionBuilder36.Selection
		
		link4 = nXObject5
		jointBuilder4.JointDefine.FirstLinkSelection.Value = link4
		
		globalSelectionBuilder37 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList36 = globalSelectionBuilder37.Selection
		
		expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		cylinder4 = part1.Features.FindObject("CYLINDER(179)")
		edge10 = cylinder4.FindObject("EDGE * 1 * 3 {(-0.5,59.1339745962156,10)(1,60,10)(-0.5,60.8660254037844,10) CYLINDER(178)}")
		point13 = workPart.Points.CreatePoint(edge10, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		edge11 = component1.FindObject("PROTO#.Features|CYLINDER(179)|EDGE * 1 * 3 {(-0.5,59.1339745962156,10)(1,60,10)(-0.5,60.8660254037844,10) CYLINDER(178)}")
		xform10, nXObject15 = workPart.Xforms.CreateExtractXform(edge11, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point14 = workPart.Points.CreatePoint(point13, xform10, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		globalSelectionBuilder38 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList37 = globalSelectionBuilder38.Selection
		
		partLoadStatus4 = part1.LoadFeatureDataForSelection()
		
		partLoadStatus4.Dispose()
		edge12 = nXObject15
		point15 = workPart.Points.CreatePoint(edge12, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		xform11, nXObject16 = workPart.Xforms.CreateExtractXform(edge11, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
		
		point16 = workPart.Points.CreatePoint(point15, xform11, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder4.JointDefine.FirstOrigin = point16
		
		origin7 = NXOpen.Point3d(0.0, 60.0, 10.000000000000002)
		xDirection4 = NXOpen.Vector3d(1.0, 0.0, 0.0)
		yDirection4 = NXOpen.Vector3d(0.0, 1.0, 0.0)
		xform12 = workPart.Xforms.CreateXform(origin7, xDirection4, yDirection4, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
		
		cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform12, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder4.JointDefine.FirstCsys = cartesianCoordinateSystem4
		
		globalSelectionBuilder39 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList38 = globalSelectionBuilder39.Selection
		
		globalSelectionBuilder40 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList39 = globalSelectionBuilder40.Selection
		
		globalSelectionBuilder41 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList40 = globalSelectionBuilder41.Selection
		
		origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
		vector4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
		direction4 = workPart.Directions.CreateDirection(origin8, vector4, NXOpen.SmartObject.UpdateOption.AfterModeling)
		
		jointBuilder4.JointDefine.FirstVector = direction4
		
		markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
		
		theSession.DeleteUndoMark(markId24, None)
		
		markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
		
		nXObject17 = jointBuilder4.Commit()
		
		theSession.DeleteUndoMark(markId25, None)
		
		theSession.SetUndoMarkName(markId23, "Joint")
		
		jointBuilder4.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression36)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.Points.DeletePoint(point14)
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression30)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression31)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression32)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression33)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression34)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression35)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Insert->Driver->Driver...
		# ----------------------------------------------
		markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		jointDriverBuilder1 = workPart.MotionManager.JointDrivers.CreateJointDriverBuilder(NXOpen.Motion.JointDriver.Null)
		
		linkDriverBuilder1 = workPart.MotionManager.LinkDrivers.CreateLinkDriverBuilder(NXOpen.Motion.LinkDriver.Null)
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.TypeOption = NXOpen.Motion.DriverOperation.Type.Polynomial
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.VelocityExpression.SetFormula("15")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.JerkExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.DisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.VelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.AccelerationExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.JerkExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.FrequencyExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.TypeOption = NXOpen.Motion.DriverOperation.Type.Undefined
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.VelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.JerkExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.BaseLinkAttachment.OrientationType = NXOpen.Motion.LinkAttachmentData.OrientationTypes.Vector
		
		linkDriverBuilder1.DriverMotions.RotationX.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationX.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationY.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.RotationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationX.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationY.ControlInitialAccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.DisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.VelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.AccelerationExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.JerkExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.AmplitudeExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.FrequencyExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.PhaseAngleExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.HarmonicDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.InitialDisplacementExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.InitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.ControlInitialVelocityExpression.SetFormula("0")
		
		linkDriverBuilder1.DriverMotions.TranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
		
		theSession.SetUndoMarkName(markId26, "Driver Dialog")
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.Function = NXOpen.NXObject.Null
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.Function = NXOpen.NXObject.Null
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.Function = NXOpen.NXObject.Null
		
		expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		linkDriverBuilder1.DriverMotions.RotationX.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.RotationX.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.RotationY.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.RotationY.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.RotationZ.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.RotationZ.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationX.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationX.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationY.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationY.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationZ.Function = NXOpen.NXObject.Null
		
		linkDriverBuilder1.DriverMotions.TranslationZ.Function = NXOpen.NXObject.Null
		
		globalSelectionBuilder42 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList41 = globalSelectionBuilder42.Selection
		
		joint1 = nXObject8
		jointDriverBuilder1.Joint.Value = joint1
		
		markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Driver")
		
		globalSelectionBuilder43 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList42 = globalSelectionBuilder43.Selection
		
		theSession.DeleteUndoMark(markId27, None)
		
		markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Driver")
		
		nXObject18 = jointDriverBuilder1.Commit()
		
		theSession.DeleteUndoMark(markId28, None)
		
		theSession.SetUndoMarkName(markId26, "Driver")
		
		jointDriverBuilder1.Destroy()
		
		linkDriverBuilder1.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression37)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression38)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Insert->Coupler->Gear Coupler...
		# ----------------------------------------------
		markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		couplerGearBuilder1 = workPart.MotionManager.Couplers.CreateCouplerGearBuilder(NXOpen.Motion.CouplerGear.Null)
		
		couplerGearBuilder1.RatioExpression.SetFormula("1")
		
		couplerGearBuilder1.FirstRadiusExpression.SetFormula("10")
		
		couplerGearBuilder1.SecondRadiusExpression.SetFormula("10")
		
		couplerGearBuilder1.DisplayScale = 1.0
		
		theSession.SetUndoMarkName(markId29, "Gear Coupler Dialog")
		
		globalSelectionBuilder44 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList43 = globalSelectionBuilder44.Selection
		
		couplerGearBuilder1.FirstJoint.Value = joint1
		
		globalSelectionBuilder45 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList44 = globalSelectionBuilder45.Selection
		
		globalSelectionBuilder46 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList45 = globalSelectionBuilder46.Selection
		
		joint2 = nXObject11
		couplerGearBuilder1.SecondJoint.Value = joint2
		
		coordinates1 = NXOpen.Point3d(0.0, 0.0, 10.000000000000002)
		point17 = workPart.Points.CreatePoint(coordinates1)
		
		globalSelectionBuilder47 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList46 = globalSelectionBuilder47.Selection
		
		markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
		
		coordinates2 = NXOpen.Point3d(0.0, 0.0, 10.000000000000002)
		point18 = workPart.Points.CreatePoint(coordinates2)
		
		nXObject19 = couplerGearBuilder1.Commit()
		
		theSession.DeleteUndoMark(markId30, None)
		
		theSession.SetUndoMarkName(markId29, "Gear Coupler")
		
		couplerGearBuilder1.Destroy()
		
		markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		couplerGearBuilder2 = workPart.MotionManager.Couplers.CreateCouplerGearBuilder(NXOpen.Motion.CouplerGear.Null)
		
		couplerGearBuilder2.RatioExpression.SetFormula("1")
		
		couplerGearBuilder2.FirstRadiusExpression.SetFormula("10")
		
		couplerGearBuilder2.SecondRadiusExpression.SetFormula("10")
		
		couplerGearBuilder2.DisplayScale = 1.0
		
		theSession.SetUndoMarkName(markId31, "Gear Coupler Dialog")
		
		# ----------------------------------------------
		#   Dialog Begin Gear Coupler
		# ----------------------------------------------
		globalSelectionBuilder48 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList47 = globalSelectionBuilder48.Selection
		
		couplerGearBuilder2.FirstJoint.Value = joint2
		
		globalSelectionBuilder49 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList48 = globalSelectionBuilder49.Selection
		
		globalSelectionBuilder50 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList49 = globalSelectionBuilder50.Selection
		
		joint3 = nXObject14
		couplerGearBuilder2.SecondJoint.Value = joint3
		
		coordinates3 = NXOpen.Point3d(0.0, 20.0, 10.000000000000002)
		point19 = workPart.Points.CreatePoint(coordinates3)
		
		globalSelectionBuilder51 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList50 = globalSelectionBuilder51.Selection
		
		markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
		
		coordinates4 = NXOpen.Point3d(0.0, 20.0, 10.000000000000002)
		point20 = workPart.Points.CreatePoint(coordinates4)
		
		nXObject20 = couplerGearBuilder2.Commit()
		
		theSession.DeleteUndoMark(markId32, None)
		
		theSession.SetUndoMarkName(markId31, "Gear Coupler")
		
		couplerGearBuilder2.Destroy()
		
		markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		couplerGearBuilder3 = workPart.MotionManager.Couplers.CreateCouplerGearBuilder(NXOpen.Motion.CouplerGear.Null)
		
		couplerGearBuilder3.RatioExpression.SetFormula("1")
		
		couplerGearBuilder3.FirstRadiusExpression.SetFormula("10")
		
		couplerGearBuilder3.SecondRadiusExpression.SetFormula("10")
		
		couplerGearBuilder3.DisplayScale = 1.0
		
		theSession.SetUndoMarkName(markId33, "Gear Coupler Dialog")
		
		# ----------------------------------------------
		#   Dialog Begin Gear Coupler
		# ----------------------------------------------
		globalSelectionBuilder52 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList51 = globalSelectionBuilder52.Selection
		
		couplerGearBuilder3.FirstJoint.Value = joint3
		
		globalSelectionBuilder53 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList52 = globalSelectionBuilder53.Selection
		
		globalSelectionBuilder54 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList53 = globalSelectionBuilder54.Selection
		
		joint4 = nXObject17
		couplerGearBuilder3.SecondJoint.Value = joint4
		
		coordinates5 = NXOpen.Point3d(0.0, 40.0, 10.000000000000002)
		point21 = workPart.Points.CreatePoint(coordinates5)
		
		markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
		
		globalSelectionBuilder55 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
		
		selectTaggedObjectList54 = globalSelectionBuilder55.Selection
		
		theSession.DeleteUndoMark(markId34, None)
		
		markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
		
		coordinates6 = NXOpen.Point3d(0.0, 40.0, 10.000000000000002)
		point22 = workPart.Points.CreatePoint(coordinates6)
		
		nXObject21 = couplerGearBuilder3.Commit()
		
		theSession.DeleteUndoMark(markId35, None)
		
		theSession.SetUndoMarkName(markId33, "Gear Coupler")
		
		couplerGearBuilder3.Destroy()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Insert->Solution->Solution...
		# ----------------------------------------------
		markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
		
		motionSolutionBuilder1 = workPart.MotionManager.MotionSolutions.CreateSolutionBuilder(NXOpen.Motion.MotionSolution.Null)
		
		theSession.SetUndoMarkName(markId36, "Solution Dialog")
		
		expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
		
		markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
		
		theSession.DeleteUndoMark(markId37, None)
		
		markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
		
		unit2 = workPart.UnitCollection.FindObject("Second")
		motionSolutionBuilder1.SetScalarExpressionPropertyValue("SolutionEndTime", "10", unit2)
		
		nXObject22 = motionSolutionBuilder1.Commit()
		
		theSession.DeleteUndoMark(markId38, None)
		
		theSession.SetUndoMarkName(markId36, "Solution")
		
		motionSolutionBuilder1.Destroy()
		
		workPart.MeasureManager.SetPartTransientModification()
		
		workPart.Expressions.Delete(expression39)
		
		workPart.MeasureManager.ClearPartTransientModification()
		
		theSession.MotionSession.MotionMethods.ModelCheck(False)
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Analysis->Motion->Solve...
		# ----------------------------------------------
		motionSolution1 = nXObject22
		motionSolution1.SolveNormalRunSolution()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Analysis->Motion->Animation Player...
		# ----------------------------------------------
		markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Animation Player")
		
		animationControl1 = motionSolution1.GetAnimationControl()
		
		markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
		
		theSession.SetUndoMarkName(markId40, "Animation Player Dialog")
		
		theSession.SetUndoMarkVisibility(markId40, None, NXOpen.Session.MarkVisibility.Invisible)
		
		theSession.MotionSession.PostProcess.SetInterferenceOption(False)
		
		theSession.MotionSession.PostProcess.SetMeasureOption(False)
		
		theSession.MotionSession.PostProcess.SetTraceOption(False)
		
		theSession.MotionSession.PostProcess.SetStopOnEventOption(False)
		
		theSession.MotionSession.PostProcess.SetInterferenceOption(False)
		
		theSession.MotionSession.PostProcess.SetMeasureOption(False)
		
		theSession.MotionSession.PostProcess.SetTraceOption(False)
		
		theSession.MotionSession.PostProcess.SetStopOnEventOption(False)
		
		animationControl1.Delay = 0
		
		animationControl1.Mode = NXOpen.Motion.PlayMode.PlayOnce
		
		animationControl1.StepToAssemblyPosition()
		
		animationControl1.Play()
		
		animationControl1.StepToAssemblyPosition()
		
		theSession.SetUndoMarkName(markId40, "Animation Player")
		
		theSession.DeleteUndoMark(markId40, None)
		
		animationControl1.Finish()
		
		theSession.CleanUpFacetedFacesAndEdges()
		
		# ----------------------------------------------
		#   Menu: Tools->Journal->Stop Recording
		# ----------------------------------------------