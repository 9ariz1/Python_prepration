#  check even or odd by function 

def chk(a):
    if a%2==0:
        return("Even Number")
    else :
        return("Odd Number")
x=int(input("Enter a number : "))
print(chk(x))