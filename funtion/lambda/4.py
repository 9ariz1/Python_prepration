
# map() function  syntax : map(function,iterable)
'''
used to perform operation on each element of collection 
'''
lst=[1,2,3,4,5,6,7,8,9,10]

# sq=list(map(lambda x : x**2,lst))
# print(sq)

def sq(n):
    return n**2

sq_r=list(map(sq,lst))
print(sq_r)