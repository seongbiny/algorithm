def fact(n):

    if n==1:
        return 1
    #5! = 5 * 4
    result = n*fact(n-1)
    return result

def fibo(n):

    if n < 2:
        return n

    r1 = fibo(n-1)
    r2 = fibo(n-2)
    return r1 + r2

print(fibo(4))
#print(fact(5))