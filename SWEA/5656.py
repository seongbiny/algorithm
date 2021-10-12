import sys
sys.stdin = open("sample_5656.txt", "r")
import copy


def drop(pos, brick):
    st = []
    # 세로 위치 찾기
    row = 0
    while row < H and brick[row][pos] == 0:
        row += 1
    if row == H: # 빈곳에 구슬 흘린것
        return
    st.append((pos, row))
    # 블럭 제거
    while st:
        curx, cury = st.pop()
        size = brick[cury][curx]
        brick[cury][curx] = 0
        # size 기분으로 삭제해야하는 것들을 스택에 넣는다
        for i in range(size):
            # 상:
            if cury - i >= 0 and brick[cury-i][curx]:
                st.append((curx, cury-i))
            # 하:
            if cury + i < H and brick[cury+i][curx]:
                st.append((curx, cury+i))
            # 좌 :
            if curx - i >= 0 and brick[cury][curx-i]:
                st.append((curx-i, cury))
            # 우:
            if curx + i < W and brick[cury][curx+i]:
                st.append((curx+i, cury))
def clean(brick):
    global minbrick
    for x in range(W):
        desp = srcp = H-1
        while srcp >= 0:
            if brick[srcp][x] > 0:
                brick[desp][x] = brick[srcp][x]
                desp -= 1
            srcp -= 1
        while desp >= 0:
            brick[desp][x] = 0
            desp -= 1

def solve(k, brick):
    global minbrick
    if k == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if brick[i][j] >= 1:
                    cnt += 1
        if cnt < minbrick:
            minbrick = cnt
        return

    for i in range(W):
        # brick 백업하고
        tmpbrick = copy.deepcopy(brick)
        res[k] = i
        drop(i, brick)
        clean(brick)
        solve(k+1, brick)
        # 복원 해준다.
        brick = copy.deepcopy(tmpbrick)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]

    res = [-1] * N
    minbrick = 99999

    solve(0, brick)
    print(f'#{tc} {minbrick}')