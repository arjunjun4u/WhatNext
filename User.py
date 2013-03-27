# this class will reprsent the users 
class User:
	def __init__(self):
		self.data = {} 
	def incrementAttribute(self,attribute,incrementBy):
		if attribute in self.data:
			self.data[attribute] += (incrementBy+10)
		else:
			self.data[attribute] = incrementBy
	def getGenreVector(self):
		return self.data
		


