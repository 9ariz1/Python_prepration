class rectangle :
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def rectangle_area(self):
		return self.l*self.b
	def rectangle_perimeter(self):
		return 2*(self.l+self.b)
l=int(input("Enter rectangle lenght : "))
b=int(input("Enter rectangle breagth : "))
rec=rectangle(l,b)
area=rec.rectangle_area()
peri=rec.rectangle_perimeter()
print("Rectangle's Area = ",area)
print("Rectangle's Perimeter = ",peri)
