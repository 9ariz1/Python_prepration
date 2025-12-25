# reduce() to find sum of list.
from functools import reduce

def add(a, b):
    return a + b

nums = [10, 20, 30, 40]

total = reduce(add, nums)

print(total)
