# method overrining 
class Square():
    def area(self,s):
        return s**2
class Rectangle(Square):
    def area(self,l,b):
        return l*b
    
sq=Square()
print(sq.area(5))

rec=Rectangle()
print(rec.area(5,6))