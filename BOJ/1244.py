# 남학생일때 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은
# 스위치를 포함하는 구간을 찾아서 그 구간에 속한 스위치의 상태를 모두 바꾼다
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다 ???????????????????????????????????




n = int(input()) # 스위치 개수
states = list(map(int, input().split()))
# 남 : 1 , 여 : 2
nums = int(input()) # 학생 수
lst = []
for i in range(nums):
    st, k = map(int, input().split())
    lst.append(st)
    lst.append(k)

for i in range(nums): # 0 1
    if lst[2*i] == 1:
        a = lst[2*i+1]  # 3
        for j in range(len(states)): # 0 1 2 3 4 5 6 7
            if j % a == 0 and j != 0:
                if states[j-1] == 1:
                    states[j-1] = 0
                elif states[j-1] == 0:
                    states[j-1] = 1
    elif lst[2*i] == 2:
        a = lst[2*i+1] # 3
        if states[a-1] == 0:
            states[a-1] = 1
        else:
            states[a-1] = 0

        idx = []
        for z in range(len(states)//2): # 0 1 2 3
            if 0 <= a-z-2 or n > a+z:    ## z 가 2 일때 a-z-2 가 -1 이 되어서 0 <= -1 조건문에 들어가면 안되는데 왜 들어가는거졍?
                if states[a-2-z] != states[a+z]:
                    if states[a-1] == 1:
                        states[a-1] = 0
                    elif states[a-1] == 0:
                        states[a-1] = 1
                elif states[a-2-z] == states[a+z]:
                    idx.append(a-2-z)
                    idx.append(a+z)
                else:
                    for j in range(idx[0], idx[-1]+1):
                        if states[j] == 1:
                            states[j] = 0
                        elif states[j] == 0:
                            states[j] = 1
            else:
                for j in range(idx[0], idx[-1]+1):
                    if states[j] == 1:
                        states[j] = 0
                    elif states[j] == 0:
                        states[j] = 1

print(states)


