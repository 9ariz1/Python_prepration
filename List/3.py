""" wap to insert dynamic value in list """

myList=[]
print("Enter 10 number in list")
for i in range(0,10):
	n=int(input())
	myList.append(n)
print(myList)
print("Max No:",max(myList))
print("Min No:",min(myList))
myList.sort()
print("List after sorting : ",myList)