# wap to sum of first natural number using while loop 
a=int(input("Enter last number of range you want to sum : "))
sum=0
i=1
while i<=a:
    print(i)
    sum=sum+i
    i+=1
print("Sum of",a,"natural number is ",sum)