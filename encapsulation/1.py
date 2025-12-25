#  Encapsulatio := in python , encapsulation is a way to restrict access to certain components of an object and prevent the accidental modification of data. It is one of the four fundamental principles of Object-Oriented Programming (OOP), along with inheritance, polymorphism, and abstraction.

# or 
#  wrapping of data into a single unit is called encapsulation 

class Car():
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def display(self):
        print(f"""Car Name : {self.name}
Model Name : {self.model}
Color : {self.color}
""")
        
scorpio=Car("Mahendra Scorpio","N- 2025","z+Black")
scorpio.display()


bmw=Car("BMW","M4","Black")
bmw.display()