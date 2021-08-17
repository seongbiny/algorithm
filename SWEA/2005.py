T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = [[0] * num for _ in range(num)]

    result = 0
    print(f'#{tc}')
    for i in range(num): # 0 1 2 3
        for j in range(num): # 0 1 2 3
            arr[i][j] = 1
            if i < j:
                arr[i][j] = 0
    #print(arr)
            if 0 < j < num-1:
                arr[i][j] = int(arr[i-1][j-1]) + int(arr[i-1][j]) # 원소+원소는 int형 일때만!

        arr[i] = list(map(str, arr[i]))
        result = ' '.join(arr[i]) # join 쓰려면 스트링이어야함
        result = result.replace('0', "") # 문자열에서 특정 원소를 제거하고싶을때 리플레이스 쓰자~

        print(result)











