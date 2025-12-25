# Destructor :- it is special type of method which is used to destroy the object and free the resources used by it

class Myclass():
    def __init__(self,name):
        self.name=name
        print("Object is created and data is stored")
    def __del__(self):
        print(f"{self.name} object is destroyed")

    def __str__(self):
        return self.name

obj1=Myclass("Aman")
print(obj1)