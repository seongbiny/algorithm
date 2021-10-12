def tour(r, c, line):
    visit = set()
    for i in range(4): # 네방향에 대해서 반복
        for _ in range(line[i]):
            r, c = r + dr[i], c + dc[i]
            if arr[r][c] in visit:
                return False
            visit.add(arr[r][c])
    return True

def check(w, h):
    # w, h 에 해당하는 사각형의 시작점을 모두 생성
    for r in range(0,N-w-h):
        for c in range(h, N-w):
            if tour(r, c, [w,h,w,h]):
                return True
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 디저트를 많이 먹으려면 사각형이 커져야함

    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    # 모든 사각형 경로를 조사해야된다.
    # 시작점 = (r, c), w, h
    # 2 <= w+h < N
    # 0 <= r < N-w-h
    # h <= c < N-w
    ans = -1
    for l in range(N-1, 1, -1): # w+h = l
        for w in range(1, l): # h = l - w
            if check(w, l-w):
                ans = l*2
                break
        if ans != -1:
            break
    print(f'#{tc} {ans}')

