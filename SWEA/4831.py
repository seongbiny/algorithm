import sys
sys.stdin = open("input_4831.txt","r")

T = int(input())
for i in range(1, T+1):
    K, N, M = map(int, input().split())
    # K = 이동할 수 있는 정거장 수 N = 정류장 종점번호 M = 충전기 설치된 정류장 갯수
    st = list(map(int, input().split())) # 충전기가 설치된 정류장 번호 리스트에 담는다

    # N에 도착하면 종료
    # 출발선에서 K 만큼 이동한다
    # 충전기 있으면 충전 없으면 -1칸씩 뒤로 간다
    # -1 칸씩 뒤로 가다가 충전기 있으면 충전하고 K 만큼 이동한다
    # -K+1 칸 뒤로 갈 동안 충전기가 없으면 0 출력

    curs = 0
    cnt = 0
    while curs < N:
        nexts = curs + K
        if nexts >= N:
            break
        if nexts in st:
            cnt += 1
            curs = nexts
        else: # nexts not in st
            for j in range(1, K): # 1 2
                # nexts - j # 5 4
                if nexts-j in st:
                    cnt += 1
                    curs = nexts-j
                elif nexts-j == curs:
                    cnt = 0
                    break
                else:
                    continue

# 왜 틀린건지 모르겠다 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




