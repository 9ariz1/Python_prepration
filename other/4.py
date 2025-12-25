# anagram str

# l1=set(input("Enter First String : ").lower().replace(" ",""))
# l2=set(input("Enter Second String : ").lower().replace(" ",""))
# # print(l2)
# if l1==l2 :
#     print("Yes")
# else :
#     print("Not")


 
l1=input("Enter First String : ").lower().strip().replace(" ","")
l2=input("Enter Second String : ").lower().strip().replace(" ","")
if sorted(l1)==sorted(l2):
    print("Anagram")
else :
    
    print("Not Anagram")