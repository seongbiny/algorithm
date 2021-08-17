import sys
sys.stdin = open('input_회문2.txt')

def check(lst): # 리스트에서 회문 길이 최댓값 뽑는 함수
    cnt = 0
    maxV = 0
    for i in range(50):
        for j in range(50):
            if lst[i:99-j] == lst[i:99-j][::-1]:
                cnt = 99-j-i
                if maxV < cnt:
                    maxV = cnt
    return maxV

T = 10
for tc in range(1, 11):

    num = input()
    arr = [input() for _ in range(100)]

    result_arr = []

    for j in range(100):
        result1 = check(arr[j])

    for i in range(100):
        newarr = []
        for j in range(100):
            newarr += arr[j][i]
        result_arr.append(''.join(newarr))
    #print(result_arr)

    for i in range(100):
        result2 = check(result_arr[i])

    if result1 > result2:
        print(f'#{tc} {result1}')
    else:
        print(f'#{tc} {result2}')

