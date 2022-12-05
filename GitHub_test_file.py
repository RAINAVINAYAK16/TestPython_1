def rec_fact(n):
    if n<=1:
        return 1
    else:
        return n*rec_fact(n-1)


****************************************

def rec_fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return rec_fib(n-1)+rec_fib(n-2)
    
******************************************

def ite_fact(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

******************************************

def ite_fib(n):
    if n==2:
        return 1
    else:
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
    return a
