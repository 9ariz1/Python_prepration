'''  exception handling '''

try :
	a=int(input("Enter A Number : "))
	b=int(input("Enter A Number : "))

	div=a/b

	print("Division = ",div)

except ValueError :
	print("Enter integers only !")

except ZeroDivisionError:
	print("Not devisble into 0")

finally :
	print("Thanks ! Visit Again")