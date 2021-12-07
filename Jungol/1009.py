while True:
    n = list(map(int, input()))
    if n == [0]:
        break

    result = ''
    sumv = sum(n)

    for i in range(len(n)-1, -1, -1):
        result += str(n[i])

    print(result, sumv)





