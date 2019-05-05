
class Screen:
	def __init__(self,buttonList,labelList,imageButtonList,imageLabelList):
		self.buttonList = buttonList
		self.labelList = labelList
		self.imageButtonList = imageButtonList
		self.imageLabelList = imageLabelList
	def addButtons(self,buttonList,imageButtonList):
		self.buttonList = buttonList	
		self.imageButtonList = imageButtonList
	def addLabels(self,labelList,imageLabelList):	
		self.labelList = labelList
		self.imagelabelList = imageLabelList
