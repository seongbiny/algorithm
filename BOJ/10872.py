def fact(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return (i*fact(i-1))

N = int(input())
print(fact(N))
