''' 
*
* *
* * *
* * * *
* * * * * '''

n=int(input("Enter a line : "))
for i in range(1,n+1,1):
	for j in range(i):
		print("*",end=" ")
	print()