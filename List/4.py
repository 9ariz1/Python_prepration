""" wap some built in fuction """

x=[10,20,30,40,50]
print(x)
print(len(x))
x.append(60)
print("After append ",x)
x.insert(2,70)
print(x)


y=['abc','def','xyz',30]
x.extend(y)
print(x)

print(x.index('abc'))

x.remove(30)
print(x)


x.pop()
print(x)

x.pop(3)
print(x)