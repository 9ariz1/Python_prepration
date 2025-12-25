
n=int(input("Enter a Number : "))
b=bin(n)
print("Binary = ",bin(n)[2:])
print("Octal = ",oct(n)[2:])
print("Hexadecimal = ",hex(n)[2:])


print("Binary = ",bin(n).replace("0b",""))