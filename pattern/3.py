'''
* 
* * 
* * *
* * * * 
* * * * *
* * * *
* * *
* *
*  '''
n=int(input("Enter a line : "))
for i in range(1,n+1,1):
	for j in range(i):
		
			print("*",end=" ")
	print()
for a in range(n-1,0,-1):
	for b in range(a):
		print("*",end=" ")
	print()