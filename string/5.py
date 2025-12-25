# wap to take input a sentence and count occurance of the word 

str=input("Enter a string : ")
b=input("Enter seacrh string : ")
x=str.lower()
a=x.split()
count=0
for i in a :
	if i==b:
		count=count+1
		#print("h")
print(count)