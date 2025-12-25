'''  wap to print daimond  
 		*
      * * *
    * * * * *
  * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
n=5
'''
n=int(input("Enter a line : "))
for i in range(1,n):
	for j in range(n-i):
		print(" ",end=" ")
	for k in range(i*2-1):
		print("*",end=" ")
	print()
for a in range(n-1,0,-1):
	for b in range(n-a):
		print(" ",end=" ")
	for c in range(a*2-1):
		print("*",end=" ")
	print()