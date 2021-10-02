T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    cnt = 0
    # m을 2로 나누는데 n만큼 반복. 쭉 나머지 1이면 온. 아니면 오프.
    for i in range(n):
        if m%2 == 1:
            m //= 2
        else:
            print(f'#{tc} OFF')
            cnt += 1
            break

    if cnt == 0:
        print(f'#{tc} ON')