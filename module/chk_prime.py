
def is_prime(n):
    if n==1 or n==0:
        print(n,"Not Prime Number")
    elif n>1 :
        for i in range(1,n+1) :
            n%i==0
            print(n,"Prime Number")
    else :
        print(n,"Not prime")