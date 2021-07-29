T = int(input())

for i in range(T):
    num = int(input())

    result = 0

    for j in range(1,num+1):
        if j % 2 == 0:
            result -= j
        else:
            result += j

    print(f'#{i+1} {result}')