# wap to print a user input table by using of while loop 
import time 
i=1
a=int(input("Enter number which you want table : "))
while i<=10 :
    print(a,"*",i,"=",a*i)
    i+=1
    time.sleep(1.5)