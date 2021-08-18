# 최대 이동 할 수 있는 만큼 전진 충전소 있으면 충전
# 충전소 없으면 뒤로 한칸 있으면 충전 없으면 뒤로 한칸
# 출발 전 정류소로 돌아오면 0 출력
import sys
sys.stdin = open("input_4831.txt","r")

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int,input().split())
    gas = list(map(int,input().split()))
    station = [0] * (n+1)
    cnt = 0
    cur = 0
    next = 0

    for i in range(len(gas)):
        station[gas[i]] = gas[i]

    while cur < n:
        next = cur + k
        if next >= n:
            break
        if station[next] in gas: # k만큼 이동했을때 충전소가 있다면
            cnt += 1
            cur = next
        else: # k만큼 이동했을때 충전소가 없다면
            for i in range(1, k): # 한칸, 한칸씩 뒤로 간다
                if station[next-i] in gas: # 뒤로 갔을때 충전소가 있다면
                    cnt += 1
                    cur = next-i
                    break  # 한칸만 뒤로 갔는데 충전소가 있다면 이 반복문을 나가야해!! 어떻게
                elif next-i-1 == cur: # 뒤로갔을때 충전소가 없다면
                    cnt = 0
                    break
        if cnt == 0:
            break

    print(f'#{tc} {cnt}')



