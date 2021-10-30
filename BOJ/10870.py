N = int(input())

def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibo(i-1) + fibo(i-2)

print(fibo(N))