# sum of nature 

def sum(n):
    if n==1 :
        return 1
    else :
        return n + sum(n-1)
    
a=int(input("Enter a range of Natural Number : "))
res=sum(a)
print(f"Sum of {a} natural number is",res)