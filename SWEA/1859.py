T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    result = 0 # 수익을 구하는 변수
    arr = lst[::-1] # 구하기 쉽게 리스트를 거꾸로 배열
    maxV = arr[0] # 맥스값을 0번째인덱스 값으로
    for i in range(len(lst)):
        if maxV > arr[i]:
            result += maxV - arr[i]
        else:
            maxV = arr[i]

    print(f'#{tc} {result}')


    # 굳이 산 값과 판 값을 일일이 구해서 서로 빼면 복잡해진다.
    # 맥스값에서 산 값을 빼주면 그게 수익이니까
    # 그 수익을 더해주면 끝