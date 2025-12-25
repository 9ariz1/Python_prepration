# function to count vowel in a string 

def cv(a):
    vowels="aeiouAEIOU"
    count=0
    for ch in a:
        if ch in vowels:
            count+=1
    return count
str=input("Enter A string : ")
print(cv(str))