import sys

num_list=[x for x in range(10)]
num_gen=(x for x in range(10))

print(sys.getsizeof(num_list))
print(sys.getsizeof(num_gen))