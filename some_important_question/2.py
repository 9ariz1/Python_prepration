class Parent:
    def add(self,a,b):
        return a-b
    

class Child(Parent):    
    def add(self,a,b):
        s=super().add(a,b)
        print(s)
        return a+b
    
p=Parent()
c=Child()
print(c.add(10,20))