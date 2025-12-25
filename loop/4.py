# wap to print rev number by user input 
num=int(input("Enter A number : "))
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
print("Reverse Number is : ",rev)