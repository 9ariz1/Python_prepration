# Build lambda-based mini calculator.

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Division not possible"

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))
