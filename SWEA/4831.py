import sys
sys.stdin = open("input_4831.txt","r")

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    # K = 이동할 수 있는 정거장 수 N = 정류장 종점번호 M = 충전기 설치된 정류장 갯수
    charge = list(map(int, input().split())) # 충전기가 설치된 정류장 번호 리스트에 담는다

    bus_stop = [0] * (n+1)

    # 충전소 표시하기
    for i in range(m):
        bus_stop[charge[i]] = 1

    # 버스의 위치
    bus_idx = 0
    ans = 0

    while True:
        # 일단 이동 버스가 이동할 수 있는 만큼은 무조건 간다.
        bus_idx += k
        if bus_idx >= n:
            break # 종점에 도착하거나 종점을 지나는 경우 종료

        for i in range(bus_idx, bus_idx-k, -1):
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break

        else:
            ans = 0
            break

    print(f'#{tc} {ans}')






