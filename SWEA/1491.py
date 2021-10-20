T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    # R*C 를 최대한 정사각형게 가깝게 만들면서 최대한 많은 타일 사용
    # 1 <= N, A, B <= 10**5
    # A*|R-C|+B*(N-R*C)

    '''
    최소값을 구해야 함
    A*|R-C| 에서 최소값 가지려면 R=C 여야함 -> 직사각형 인테리어니까 조건이 안맞음
    B*(N-R*C) 에서 최소값 가지려면 N = R*C 여야함 -> 이거 이용해야함
    R, N/R 
    '''
    result = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if N >= r * c:
                result.append(A * abs(r - c) + B * (N - r * c))
            else:
                break # 제한시간 초과나서 break 조건 추가
    print(f'#{tc} {min(result)}')

