class Employee():
    company="SoftPro India"
    def __init__(self,id,name,salary):
        self.empid=id
        self.empname=name
        self.salary=salary
    def showinfo(self):
        print("Companyy Name : ",self.company)
        print("Id :- ",self.empid)
        print("Name :- ",self.empname)
        print("Salary :- ",self.salary)

a=int(input("Enter Id : "))
b=input("Enter Name : ")
c=int(input("Enter Salary : "))
obj1=Employee(a,b,c)
obj1.showinfo()
