#Genrator (use to memory outimaization)

# start fun --> excute yield --> 


def simple_genrator(n):
    for i in range(1,n+1):
        yield i

gen=simple_genrator(10)

print(next(gen))

s=0
for i in gen:
    s=s+i

print(s)