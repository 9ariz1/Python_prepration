''' Multi level '''



class A :
	def m1(self):
		print("M1 is function of class A")
class B(A) :
	def m2(self):
		print("M2 is function of class B")
class C(B) :
	def m3(self):
		print("M3 is function of class C")
c=C()
c.m3()
c.m2()
c.m1()