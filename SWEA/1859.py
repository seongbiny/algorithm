T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    result = 0
    arr = lst[::-1]
    maxV = arr[0]
    for i in range(len(lst)):
        if maxV > arr[i]:
            result += maxV - arr[i]
        else:
            maxV = arr[i]

    print(f'#{tc} {result}')