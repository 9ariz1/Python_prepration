'''statics variable= called in class
   non statics variable= class in class with self perameter '''

class Employee :
	def setvalue(self,empid,empname,empsal):
		self.empid=empid			# non statics variable
		self.empname=empname
		self.empsal=empsal
	def getvalue(self):
		print("Employee Id : ",self.empid)
		print("Employee Name : ",self.empname)
		print("Employee Salary : ",self.empsal)
id=int(input("Enter Id : "))
name=input("Enter Name : ")
sal=int(input("Enter Salary : "))
e=Employee()
e.setvalue(id,name,sal)
e.getvalue()	