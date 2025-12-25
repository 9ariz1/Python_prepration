'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
r=int(input("Enter number of row : "))
c=int(input("Enter number of colunm : "))
for i in range(1,r+1):
	for j in range(1,c+1):
		if i==1 or i==r or j==1 or j==c:
			print("*",end=" ")
		else :
			print(" ",end=" ")
	print()