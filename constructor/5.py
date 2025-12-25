class Rectangle():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def area(self):
        return self.a*self.b
    
x=int(input("Enter lenght of Rectengle : "))
y=int(input("Enter lenght of Rectengle : "))

ar=Rectangle(x,y)
print(f"Area of Rectangle {x} and {y} is {ar.area()}")