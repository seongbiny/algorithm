n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(input())

cnt_W = 0
cnt_B = 0

if m%2==0:
    check_1 = ['W', 'B'] * (m // 2)
    check_2 = ['B', 'W'] * (m // 2)
else:
    check_1 = ['W', 'B'] * (m // 2)
    check_1.append('W')
    check_2 = ['B', 'W'] * (m // 2)
    check_2.append('B')

for i in range(n):
    for j in range(m):
        if i%2==0:
            if arr[i][j] != check_1[j]:
                cnt_W += 1
            if arr[i][j] != check_2[j]:
                cnt_B += 1
        else:
            if arr[i][j] != check_2[j]:
                cnt_W += 1
            if arr[i][j] != check_1[j]:
                cnt_B += 1

print(min(cnt_B, cnt_W))



# 8*8 크기의 체스판을 만들어야함