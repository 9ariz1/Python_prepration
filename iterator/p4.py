
def infinite_number():
    num=1
    while True :
        yield num
        num+=1

for n in infinite_number():
    if n>10:
        break
    print(n)

gen=infinite_number()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
