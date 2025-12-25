# filter() to extract odd numbers from list.
def is_odd(n):
    return n%2!=0
nums=[1,2,3,4,5,6,7,8,9]
odd=list(filter(is_odd,nums))
print(odd)