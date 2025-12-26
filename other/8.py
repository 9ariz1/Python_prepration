import random 
# otp=random.randint(1000,9999)

# print(otp)

otp=""
for i in range(6):
    otp+=str(random.randint(0,9))
print(otp)
    