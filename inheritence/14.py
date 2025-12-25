
class Shape():
    def Setvalue(self,a):
        self.a=a

class Square(Shape):
    def area(self):
        return self.a*self.a
    
class Cube(Shape):
    def volume(self):
        return self.a**3

c=Cube()
c.Setvalue(3)
print(f"Square : ",c.volume())

s=Square()
s.Setvalue(4)
print(f"Cube : ",s.area())