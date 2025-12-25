# method overloading 

class Shape():
    def area(self,*args):
        if len(args)==1:
            return args[0]**2
        elif len(args)==2:
            return args[0]*args[1]
    # def area(self,a=None,b=None):        # default perameter
    #     if a is not None and b is None:
    #         return a**2
    #     elif a is not None and b is not None :
    #         return a*b
        

sh=Shape()
print(sh.area(5))
print(sh.area(5,6))