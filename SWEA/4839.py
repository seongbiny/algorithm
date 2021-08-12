def binaryS(r, key):
    start = 1
    end = r
    cnt = 0
    middle = (start + end) // 2
    while middle != key:
        if middle == key:
            cnt += 1
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
        middle = (start + end) // 2 # 왜 넣어주는거임?
    return cnt

T = int(input())

for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())
    # p : 전체 쪽 수 pa : a가 찾아야 하는 쪽 수 pb : b가 찾아야 하는 쪽 수
    result = 0

    if binaryS(p, pa) < binaryS(p, pb):
        print(f'#{tc} A')
    elif binaryS(p, pa) > binaryS(p, pb):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')







