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

def fibo_m():
    #if n < 2:
    #    memo[n] = n
    #    return memo[n]

    if memo[n] > 0: #값이 있으면:
        return memo[n]
    else:
        memo[n] = fibo_m(n-1) + fibo(n-2)
        return memo[n]

    if n >= 2 and memo[n] == 0:
        memo[n] = fibo_m(n - 1) + fibo_m(n - 2)
    return memo[n]

n = 10
memo = [0] * (n+1) # n까지 쓸수 있는 빈공감
memo[0] = 0
memo[1] = 1
fibo(10)

