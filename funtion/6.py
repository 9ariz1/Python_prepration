# non paremeterized
def greed():
    print("Good After Noon")

greed()

# Paremeterized
def greed(name):
    print("Good AfterNoon",name)

greed("Rohit")


# return type 

def greed():
    return "Good AfterNoon "

print(greed())

# Non Return Type 

def greed(name):
    return "Good Afternoon "+ name

print(greed("Mohammad Ariz"))
