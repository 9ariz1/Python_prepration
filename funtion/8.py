# create two function ftoc and ctof both perameterized and return type 

def ftoc(n):
    return (n-32)*5/9


def ctof(m):
    return (m*9/5)+32

print("Enter 1 for c To F \n Enter 2 for C to F ")

ch=int(input("Enter Choise : "))
if ch==1 :
    m=int(input("Enter tempture in Celsius : "))
    print("C to F : ",ctof(m))
elif ch==2 :
    n=int(input("Enter tempture in Farenhiet : "))
    print("F to C : ",ftoc(n))

else :
    print("Invailid Choice ")