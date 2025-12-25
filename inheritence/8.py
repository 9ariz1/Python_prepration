class Parent():
    def sayhello(self):
        print("Hello....")
class Child(Parent):
    def saygb(self):
        print("Good Bye......")

c=Child()
c.sayhello()
c.saygb()