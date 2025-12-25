''' multiple inheritence '''

class A :
	def m1(self):
		print("I am function M1 of the class A")
class B :
	def m2(self):
		print("I am function M2 of the class B")
class C (A,B) :
	def m3(self):
		print("I am function M3 of the class C")
c=C()
c.m3()
c.m1()
c.m2()