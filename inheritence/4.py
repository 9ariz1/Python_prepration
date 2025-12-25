class Base:
	def showBase(self):
		print("This massage form Base class")
class Derived (Base):
	def showDerived(self):
		print("This massage from Derived class")

d=Derived()
d.showDerived()
d.showBase()