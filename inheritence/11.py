# hybrid Inheritence 

class A():
    def m1(self):
        print("M1 from class A")
class B(A):
    def m2(self):
        print("M2 from class B")

class C(B):
    def m3(self):
        print("M3 from class C")

class D(C,A):
    def m4(self):
        print("M4 from class D")

d=D()
d.m4()
d.m3()
d.m2()
d.m1()