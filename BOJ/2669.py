square = [[0] * 4 for _ in range(4)]

arr = [[0] * 100 for _ in range(100)]

for i in range(4):
    square = list(map(int, input().split()))
# square2 = list(map(int, input().split()))
# square3 = list(map(int, input().split()))
# square4 = list(map(int, input().split()))
    #print(square)  # [1, 2, 4, 4]
    # 13 23 33
    # 12 22 32
    for x in range(square[0], square[2]): # 1, 4
        for y in range(square[1], square[3]): # 2, 4
            if arr[x][y] == 1:
                pass
            arr[x][y] = 1
#print(arr)
sum = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum += arr[i][j]
print(sum)









