# Multilevel

class A ():
    def m1(self):
        print("M1 is method of class A")

class B():
    def m2(self):
        print("M2 is method of class B")

class C(A,B):
    def m3(self):
        print("M3 is method of class C")

c=C()
c.m3()
c.m1()
c.m2()