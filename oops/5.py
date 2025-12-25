class cuboid:
	def __init__(self,l,b,h):
		self.l=l
		self.b=b
		self.h=h
	def cvol(self):
		return self.l*self.b*self.h
a=int(input("Enter lenght : "))
b=int(input("Enter breaght : "))
c=int(input("Enter hieght : "))
c=cuboid(a,b,c)
val=c.cvol()
print("Valunm of Coboid : ",val)