# hierarchy inheritence

class Shape:
	def setValue(self,a):
		self.a=a
class Square(Shape):
	def area(self):
		b=self.a*self.a
		print("Area of Square : ",b)
class Cube(Shape):
	def volume(self):
		h=self.a*self.a*self.a
		print("Volume of Cube : ",h)
		
n=eval(input("Enter A redius : "))
c=Cube()
c.setValue(n)
c.volume()
s=Square()
s.setValue(n)
s.area()