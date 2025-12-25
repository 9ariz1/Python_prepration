""" wap to take a list of your friends and sort it in alpabatical order """

list=[]
for i in range(1,5):
    n=input("Enter your friend name : ")
    list.append(n)
print(list)

list.sort()
print("After sorting list alphabetic according : ",list)