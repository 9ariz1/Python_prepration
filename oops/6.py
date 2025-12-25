class Student:
	def __init__(self,name,rollno,fee):
		self.name=name
		self.rollno=rollno
		self.fee=fee
	def display(self):
		print("Student name is : ",self.name)
		print("Student Roll No is : ",self.rollno)
		print("Student Fee is : ",self.fee)
name=input("Enter Student Name : ")
rol=int(input("Enter Student Roll NO : "))
fee=int(input("Enter Student FEE : "))
s=Student(name,rol,fee)
s.display()