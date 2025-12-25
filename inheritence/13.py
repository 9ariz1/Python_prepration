# write a python program to create a class named base . In base class create a method showbase(), this method display a massege "This massage from base class ". By inheriting base class now create a class name derived . In derived class create a method showderived(), this method display a massage "This massage from derived class", now test Base and Derived class.

class Base():
    def showbase(self):
        print("This massage from base class")

class Derived(Base):
    def showderived(self):
        print("This massage from Derived class")

d=Derived()
d.showderived()
d.showbase()