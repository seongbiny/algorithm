T = int(input())

for i in range(T):
    result = input()
    a = list(result)
    cnt = 0
    sum = 0
    for j in a:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)

