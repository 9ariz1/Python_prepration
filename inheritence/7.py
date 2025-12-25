# hybrid inheritance

class Employee:
	def info(self):
		print("Information")
class Manager(Employee):
	def mg(self):
		print("Manager Class")
class Tech(Employee):
	def eg(self):
		print("Engineer Class")
class Team(Manager,Tech):
	def tl(self):
		print("Team Leader")

t=Team()
t.tl()
t.eg()
t.mg()
t.info()