T = int(input())
for tc in range(1, T+1):
    N = int(input())

    num = list(map(int, input().split()))

    def bubble(arr):
        for i in range(len(arr)-1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


    #a = ' '.join(str(z) for z in bubble(num))

    #for z in bubble(num):
    #    a = str(z)
    #result = ' '.join(a)
    result = ' '.join(map(str, bubble(num)))

    #print(*bubble(num))
    print(f'#{tc} {result}')

    def lowbubble(arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i, i, -1):
                if arr[j] > arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]