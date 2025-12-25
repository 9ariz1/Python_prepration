from abc import ABC , abstractmethod

class Shape (ABC) :
    #@abstractmethod
    def area(self,l,b):
        pass
    #@abstractmethod
    def perimeter(self,l,b):
        pass

class rectangle(Shape):

    def area(self,l,b):
        return l*b

    def perimeter(self,l,b):
        return 2*(l+b)

l=int(input("Enter lenght : "))
b=int(input("Enter lenght : "))
c=rectangle()
print(f"Area of Rectangle where lenght is {l} and width is {b} = {c.area(l,b)}")
print(f"PErimeter of Rectangle where lenght is {l} and width is {b} = {c.perimeter(l,b)}")