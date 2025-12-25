'''
* 
* * 
* * *
* * * * 
* * * * *
* * * *
* * *
* *
*  
* 
* * 
* * *
* * * * 
* * * * *
* * * *
* * *
* *
*  '''

n=int(input("enter a line : "))
for i in range(1,n+1,1):
	for j in range(i):
		
			print("*",end=" ")
	print()
for a in range(n-1,0,-1):
	for b in range(a):
		print("*",end=" ")
	print()
for c in range(1,n+1,1):
	for d in range(c):
		
			print("*",end=" ")
	print()
for e in range(n-1,0,-1):
	for f in range(e):
		print("*",end=" ")
	print()