

sent="   The sun rises in the east".strip() # remove whitespace

words=sent.split(" ")  # return a list based on the seprator 
print(sent)
print(words)

print("Word Count = ",len(words))

#print(count(words))

ch=0
ws=0

for c in sent :
    if c.isspace():
        ws+=1
    else :
        ch+=1
print(ch,ws)




char=[]

for c in sent:
    if not c.isspace():
        char.append(c)
print(char)