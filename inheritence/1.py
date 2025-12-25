''' Inheritence 
type of inheritence 
1.Single level
2.Multi level
3.Multiple level
4.Hierarchy level 
5.Hybrid 


Single level inheritance 
'''


class BollDog:
	def grawl(self):
		print("Bruno")
		print("Gurrrrr.........Gurrrrr...........")
class RunDog(BollDog):
	def bark(self):
		print("Sheru.....")
		print("Bhooo...Bhooo...")
Dog=RunDog()
Dog.bark()
Dog.grawl()