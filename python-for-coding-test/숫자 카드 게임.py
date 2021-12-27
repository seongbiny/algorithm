n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
for i in range(n):
    pick = min(arr[i])
    maxV = max(maxV, pick)

print(maxV)

'''
문제가 한 번 읽고 바로 이해가 되지 않음
두세번 더 읽어보고 이해했다.
각 행마다 가장 작은 카드를 뽑아서 그 중 제일 큰 숫자를 프린트.
'''