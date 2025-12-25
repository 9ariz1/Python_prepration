# wap to take string as input to check string is polindrome or not 

str=input("Enter a string : ")
a=str.lower()
str_rev="".join(reversed(a))
#print(str_rev)

if a==str_rev:
	print(str,"is Polindrome")
else :
	print(str,"is not Polindrome")