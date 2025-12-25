'''
* * * * *
* *   * *
*   *   *
* *   * *
* * * * *
'''
r=5
c=5
for i in range(1,6):
	for j in range(1,6):
		if i==1 or i==5 or j==1 or j==5 or i==2 and j==2 or i==2 and j==4 or i==3 and j==3 or i==4 and j==2 or i==4 and j==4:
			print("*",end=" ")
		else :
			print(" ",end=" ")
	print()