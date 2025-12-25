# map() to convert Celsius to Fahrenheit list.

def ctof(c):
    return (c * 9/5) + 32

c_lst= [0, 10, 20, 30, 40]
f_lst = list(map(ctof,c_lst))

print(f_lst)
