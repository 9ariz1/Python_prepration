# binary to decimal 

a=int(input("Enter a Binary number : "))
p=0
dec=0
# while a>0:
#     d=a%10
#     dec=dec+d*2**p
#     p+=1
#     a//=10
for d in str(a)[::-1]:
    dec=dec+int(d)*2**p
    p+=1
print(dec)
