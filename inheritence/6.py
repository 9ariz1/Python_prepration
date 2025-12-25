class Employee:
	def setemp(self,empId,empName):
		self.empid=empId
		self.empname=empName
	def getemp(self):
		print("Employee Id : ",self.empid)
		print("Employee Name : ",self.empname)
class Payroll(Employee):
	def setPayroll(self,bs,hra,da):
		self.bs=bs
		self.hra=hra
		self.da=da
	def getPayroll(self):
		print("Basic Salary : ",self.bs)
		print("HRA : ",self.hra)
		print("DA : ",self.da)
class Payslip(Payroll):
	def netSalary(self):
		netS=self.bs+self.hra+self.da
		print("Total Salary : ",netS)
name=input("Enter Enployee Name : ")
roll=int(input("Enter Employee ID : "))
hra=int(input("Enter HRA : "))
bs=int(input("Enter BS : "))
da=int(input("Enter DA : "))
p=Payslip()
p.setemp(name,roll)
p.getemp()
p.setPayroll(hra,bs,da)
p.getPayroll()
p.netSalary()