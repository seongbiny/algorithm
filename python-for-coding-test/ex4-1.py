# 입력부
N = int(input())
plan = input().split()
# 출발지점 인덱스
x,y = 1,1
# 방향
direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 계획 실행
for i in plan:
    for d in range(len(direction)):
        if i == direction[d]:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 < nx < N and 0 < ny < N:
                x, y = nx, ny

print(x, y)


# pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행
# continue : 바로 다음 순번의 loop를 수행
# break : 반복문을 멈추고 loop 밖으로 나감