'''
# 재귀로 점화식을 이용해서 푸는 문제
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + 2*paper(n-2)

T = int(input())
for tc in range(1, T+1):
    num = int(input())

    print(f'#{tc} {paper(num//10)}')
'''

#dp로 푸는 것

T = int(input())
arr = [0] * 32
arr[1] = 1
arr[2] = 3
for n in range(1, 31):
    arr[n] = arr[n-1] + 2*arr[n-2]
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc} {arr[n]}')


