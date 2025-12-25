# wap to check the number is present in the list or not 

list=[]

a=int(input("Enter these number you want list range : "))
for i in range(0,a):
    n=int(input("Enter number : "))
    list.append(n)
print(list)

num=int(input("Enter these number you want to check in list : "))

for i in range(0,a):
    if num==list[i]:
        print(num,"is present in ",list)
        break
else :
    print(num,"is not present in ",list)