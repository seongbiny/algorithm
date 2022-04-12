'''
끝나는 시간 오름차순으로 정렬한 후
끝나는시간 <= 시작하는 시간 의 개수를 세준다
'''

n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]
table.sort(key=lambda x: (x[1], x[0]))

# i = 0
# cnt = 1
# while i != n-1:
#     for j in range(i, n):
#         if table[i][1] <= table[j][0]:
#             cnt += 1
#             i = j

cnt = 1
endtime = table[0][1]
for i in range(1,n):
    if endtime <= table[i][0]:
        cnt += 1
        endtime = table[i][1]

print(cnt)