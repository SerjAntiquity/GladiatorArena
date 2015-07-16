class Deleter():
	def __init__(self, gladiatorList):
		self.gladiatorList = gladiatorList

	def listGladiator(self):
		if len(self.gladiatorList) == 0:
			print("Нет созданных гладиаторов, нечего удалять")
			return
		else:
			print("work")
