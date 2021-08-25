row, col = map(int, input().split())

cut = int(input())
# 가로 = 0 세로 = 1
arr = [[0] * row for _ in range(col)]
cut_arr = []
for i in range(cut):
    x = list(map(int, input().split()))
    cut_arr.append(x)

#print(cut_arr)
# [[0, 3], [1, 4], [0, 2]]
row_lst = []
col_lst = []
side_lst = [[0,0],[0,row-1],[col-1,0],[col-1,row-1]]
for i in range(cut): # 0 1 2
    if cut_arr[i][0] == 0: # 가로로 자르기
        row_lst.append(cut_arr[i][1])
    if cut_arr[i][0] == 1: # 세로로 자르기
        col_lst.append(cut_arr[i][1])

각 사이드 양 끝 점이랑 가로세로 교차점까지 넓이 구하면 . . .될거같은데 ㅋ