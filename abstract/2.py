from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peri(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
    def peri(self):
        return 2*3.14*self.r
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def peri(self):
        return 2*(self.l+self.b)
    
c=Circle(3)
print(f"Area of Circle : ",c.area())
print(f"Perimeter of circle : ",c.peri())

r=Rectangle(4,5)
print(f"Area of Rectangle : ",r.area())
print(f"Perimeter of Rectangle : ",r.peri())