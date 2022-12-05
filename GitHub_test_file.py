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