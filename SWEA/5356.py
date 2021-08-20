T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    maxV = 0
    for i in range(len(arr)):
        if maxV < len(arr[i]):
            maxV = len(arr[i])

    for i in range(len(arr)):
        while len(arr[i]) != maxV:
            arr[i].append(' ')

    result = ''

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            result += arr[j][i]

    #result = ''.join(result)
    result = result.replace(" ", "")
    print(f'#{tc} {result}')