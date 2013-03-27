# this class will reprsent the users 
class Thingy:	
	def __init__(self,name):
		self.data = {} 
		self.name = name 
	def isLike(self,attribute,incrementBy):
		if attribute in self.data:
			self.data[attribute] += (incrementBy+10)
		else:
			self.data[attribute] = incrementBy
	def definedLike(self):
		return self.data			
		
	def isNotLike(self,attribute):
		if attribute in self.data:
			self.data.pop(attribute)


