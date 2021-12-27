n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

result = 0
cnt = 0
for i in range(m):
    if cnt != k:
        result += lst[-1]
        cnt += 1
    else:
        cnt = 0
        result += lst[-2]

print(result)


'''
# 1
리스트를 오름차순으로 정렬한 후 큰 숫자부터 k번씩 더해주고, 작은 숫자로 내려가는 반복문을 썼다.
문제를 다시 읽어보니 그냥 가장 큰 수와 두번째로 큰 수만 있으면 풀 수 있는 문제였다.
'''