
dict1={
    '1':20,
    '2':30,
    '3':40
}
for k,v in dict1.items():
    print(k,v)

#adding
dict1['4']=50
dict1.update({'5':60,'7':80})
print(dict1)

# get the element 

print(dict1['9']) # KeyError: '9'

print(dict1.get('6')) # get return output none without showing error 