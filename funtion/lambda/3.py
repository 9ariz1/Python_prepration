
# using filter find the even in list use expression in python

lst=[1,2,3,4,5,6,7,8,9,10]
# sq=list(filter(lambda x : x%2==0 , lst ))
# print(sq)

def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2==1

even_num=list(filter(is_even,lst))
odd_num=list(filter(is_odd,lst))
print(even_num)
print(odd_num)