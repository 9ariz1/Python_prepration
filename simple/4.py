''' swap two number '''
# swap
# (a,b=b,a)

# (temp=b
# a=b
# b=temp)

a=int(input("Enter first Number : "))
b=int(input("Enter second numner : "))
temp=a
a=b
b=temp
print("After swapping ",a,b)