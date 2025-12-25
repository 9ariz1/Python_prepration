# handling file not found exception 
filename=input("Enter File Name Here : ")
f=None
try:
    f=open(filename,"r")
    data=f.read()
    print(data)
except FileNotFoundError :
    print("This Is File doesn't exists.")

finally:
    if f is not None:
        f.close()
