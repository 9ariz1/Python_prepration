# Recursion 


def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1)
    
a=int(input("Enter A Number : "))
res=fact(a)
print(f"factorial of {a} is ", res)