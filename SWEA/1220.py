import sys
sys.stdin = open("input_1220.txt", "r")

# 열에서만 움직이니까 열 우선 순회를 해야한다.
# 굳이 한칸씩 직접 이동시킬 필요 없이
# n극 아래 s 극이 있다는 한 쌍을 찾으면 그게 교착상태 1로 체크하면 된다.

#인풋에 숫자가 다 붙어있는데 떨어뜨려서 리스트에 담아야하면 스플릿을 빼면돼

T = 10
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        flag = 0 # 열마다 초기화
        for j in range(n):
            if flag == 0 and arr[j][i] == 1:
                flag = 1
            elif flag == 1 and arr[j][i] == 2:
                cnt += 1
                flag = 0

    print(f'#{tc} {cnt}')


