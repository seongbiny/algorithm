def search(start):
    cnt = 1
    y = 0 # 행
    x = start # 열
    while y < 99:
        y += 1
        cnt += 1
        # 왼쪽길이 나타나면 계속 왼쪽으로 간다
        if x > 0 and ladder[y][x-1] == 1:
            while x > 0 and ladder[y][x-1] == 1:
                x -= 1
                cnt += 1
        # 오른쪽길이 나타나면 계속 오른쪽으로 간다
        elif x < 99 and ladder[y][x+1] == 1:
            while x < 99 and ladder[y][x+1] == 1:
                x += 1
                cnt += 1
        # 왼쪽, 오른쪽 길 둘 다 없으면 아래로 내려간다
    return cnt # 이동한 거리 체크

for tc in range(1, 11):
    n = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    cnt = 100*100 # 갈수있는 최대 거리
    x = 0
    for i in range(100):
        if ladder[0][i] == 1:
            if cnt > search(i):
                cnt = search(i)
                x = i

    print(f'#{tc} {x}')



