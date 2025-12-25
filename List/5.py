""" wap to user five dynamic number and sum of these number """

list=[]
sum=0
print("Enter five number : ")
for i in range(0,5):
    n=int(input())
    list.append(n)
print("List : ",list)

for i in range(0,5):
    sum=sum+list[i]
print("Sum of list number : ",sum)