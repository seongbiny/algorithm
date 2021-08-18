import sys
sys.stdin = open("input_1983.txt","r")

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        m, f, h = list(map(int, input().split()))
        score = m*0.35 + f*0.45 + h*0.2
        arr.append(score)
    z = arr[k-1] # k번째 학생의 점수
    num = n // 10

    # 점수순대로 정렬
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    idx = 0
    for i in range(len(arr)):
        if arr[i] == z:
            idx = i # k번째 학생의 점수가 담겨있는 인덱스 획득

    # 정렬한 리스트랑 점수표랑 매치
    # a+a+ a0a0 a-a- b+b+ ...

    new = []
    for i in range(len(grades)): # 1,2
        for j in range(1, num+1):
            new.append(grades[i])
    #print(new)

    print(f'#{tc} {new[idx]}')



