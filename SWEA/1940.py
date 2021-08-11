T = int(input())
for tc in range(1, T+1):
    N = int(input())

    speed = 0 # 속도 담을 변수
    result = 0 # 속도를 다 더하면 이동한 거리

    for i in range(N):
        command = list(map(int,input().split()))
        #가속일때
        if command[0] == 1:
            speed += command[1]
        #감속일때
        elif command[0] == 2:
            if speed < command[1]: # 제약사항 3번
                speed = 0
            else: # 현재 속도보다 감속할 속도가 더 작다.
                speed -= command[1]
        result += speed
    print(f'#{tc} {result}')
'''
5
1 2   2
1 2   2+4 = 6
2 1   2+4+3 = 9
0     2+4+3+3 = 12
0     2+4+3+3+3 = 15
'''




