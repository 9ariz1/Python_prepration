class bank: 
	def __init__(self,acno,name,bal):
		self.acno=acno
		self.name=name
		self.bal=bal
	def deposite(self,dipo):
		self.dipo=dipo
		return self.bal+self.dipo
	def withdraw(self,w):
		if self.bal>=w:
			self.withdraw=w
			return self.bal-self.withdraw
		else :
			return "Insufficient Balance."
	def enquiry(self,acno,name,bal):
		print("Account Number is : ",self.acno)
		print("Account Holder Name is : ",self.name)
		print("Account Balance is :",self.bal)
acno=int(input("Enter Customer Account NO : "))
name=input("Enter Customer Name : ")
balance=eval(input("Enter Customer Balance : "))
b=bank(acno,name,balance)
print("Press 1 for deposite opration.")
print("Press 2 for withdraw opration.")
print("Press 3 for Enquiry opration.")
n=int(input("Press no for required opration : "))
if n==1:
  d=int(input("Enter Diposit Amount : "))
  x=b.deposite(d)
  print("Total Amount after Deposit in Bank : ",x)
elif n==2:
  w=int(input("Enter  WithDraw amount : "))
  y=b.withdraw(w)
  print("Total Balance after withdraw : ",y)
elif n==3:
    b.enquiry(acno,name,balance)
else:
  print("Plzz press any 1/2/3 number for required opration.")
