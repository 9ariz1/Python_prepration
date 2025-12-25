''' take full name as input & print short name 
Mohd Asif Ansari =M. A. Ansari
Mohammad Asif = M. Asif
'''

a=input("Enter Full Name : ").title().split(" ")
short_name=""
for i in a[0:len(a)-1]:
    short_name=short_name+i[0]+". "

short_name=short_name+a[-1]
print(short_name)

# a=input("Enter Full Name : ").title()
# b=a.split(" ")
# short_name=""
# for i in b[0:len(b)-1]:
#     short_name=short_name+i[0]+". "

# short_name=short_name+b[-1]
# print(short_name)

