# fibonacci series 

def fibo(n):
    if n<=1 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)
    
n=int(input("Enter a number : "))
# a=0
# b=1
list=[]
for i in range(n):
    list.append(fibo(i))
print(f" Fibonacci Series is {list}")