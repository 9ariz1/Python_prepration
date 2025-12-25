
class A:
    def add(self,a,b):
        return a-b
    
class B(A):
    def add(self,a,b):
        s=super().add(a,b)
        print(s)
        return a+b

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
obj=B()
print(obj.add(a,b))
