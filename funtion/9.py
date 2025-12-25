# function with *argument 

def add_number(*agr):
    total=0
    for num in agr :
        total+=num
    return total


result =add_number(10,20,30,40,50)
print(result)