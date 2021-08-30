# 1차원 리스트를 풀어서 홀수면 세기-> cnt 이용
arr = [3, 4, 5, 7, 7, 5]
cnt = 0
for i in arr:
    if i % 2 != 0:
        cnt += 1
print(cnt)

# while을 이용하여 인덱스 접근으로 특정조건을 만족하면 세기
arr = [3, 4, 5, 7, 7, 7, 5]
cnt = 0
i = 0
while i < len(arr):
    if arr[i] == 7:
        cnt += 1
    i += 1
print(cnt)

# 1차원 리스트를 풀어 값 접근으로 특정조건을 만족하며 세기
arr = [3, 4, 5, 7, 7, 7, 5]
cnt = 0
for i in arr:
    if i == 7:
        cnt += 1
print(cnt)

# 2차원 리스트에서 특정조건을 만족하면 세기
arr = [
    [3, 2, 5, 9],
    [1, 2, 3, 4],
    [5, 5, 7, 7],
]
cnt = 0
# 행우선 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if 3 <= arr[i][j] <= 4:
            cnt += 1
print(cnt)

# flag를 활용하여 조건문 활용
arr = [3, 2, 7, 5, 3, 7, 1]
flag = False
for i in range(len(arr)):
    if arr[i] == 7:
        flag = True
        break
if flag == 0:
    print('안존재')
else:
    print('존재')

# 2차원 리스트에서 flag로 조건문 활용
arr = [
    [3, 2, 5, 9],
    [1, 2, 3, 4],
    [5, 5, 7, 7],
]
flag = False
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 7:
            flag = True
            break
    if flag == 1:
        break
if flag == 0:
    print('안존재')
else:
    print('존재')

# 공백으로 구분된 2차원 리스트 입력하기
arr = [list(map(int, input().split())) for _ in range(3)]
de = -1
print(arr)

s = 'ATCKB'
arr = [[s] for _ in range(5)]
i = 0
arr1 = [[s] for _ in range(len(arr)) if len(arr) >= 0]
print(arr)
print(arr1)

# 1차원 리스트 프린트 하는 방법
s = 'ATCKB'
for i in range(4, -1, -1):
    for j in range(0, i+1):
        print(s[j], end='')
    print()

for i in range(5):
    for j in range(i, 5):
        print(s[j], end='')
    print()

# 1차원 리스트 채우는 방법
lst = [0] * 6
num = int(input())
t = num
for i in range(6):
    lst[i] = t
    t += 2
print(lst)

s = int(input())
arr = []
while len(arr) < 6:
    arr.append(s)
    s += 2
print(arr)

# 1차원 리스트
def is_exist(s):
    for i in len(s):
        if s[i] == 7:
            return 1
    return 0 # for문을 다 돌았는데 없다

s = [3, 2, 1, 7, 5, 9]
is_exist(s)

def is_exist(s):
    global cnt
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 7:
                cnt += 1
    return print(f'{cnt}')

s = [
    [3, 2, 1, 7],
    [1, 2, 3, 4],
    [7, 5, 2, 1],
]
cnt = 0
is_exist(s)

# 함수 활용
def is_same():
    for i in range(5):
        if lst1[i] != lst2[i]:
            return 0
    return 1
lst1 = [3, 2, 7, 5, 9]
lst2 = [3, 2, 7, 3, 9]

ret = is_same()
if ret == 1:
    print('동일')
else:
    print('안동일')

def is_same():
    global cnt
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == arr[-1][j]:
                cnt += 1
                return 1
    return 0
arr = [
    [3,2,1,7,9],
    [1,2,3,4,5],
    [3,2,1,7,9],
    [4,3,2,1,0],
    [3,2,1,6,9],
    [3,2,1,7,9]
]
cnt = 0
ret = is_same()
if ret == 1:
    print('동일')
else:
    print('안동일')

def is_same(row):
    for c in range(5):
        if arr[0][c] != arr[row][c]:
            return 0
    return 1
arr = [
    [3,2,1,7,9],
    [1,2,3,4,5],
    [3,2,1,7,9],
    [4,3,2,1,0],
    [3,2,1,6,9],
    [3,2,1,7,9]
]
cnt = 0
for row in range(1, 6):
    ret = is_same(row)
    if ret == 1:
        cnt += 1
print(cnt)

def is_same(row):
    for col in range(5):
        if apart[0][col] != apart[row][col]:
            return 0
    return 1
apart = [
    [3,2,1,7,9],
    [1,2,3,4,5],
    [3,2,1,7,9],
    [4,3,2,1,0],
    [3,2,1,6,9],
    [3,2,1,7,9]
]
cnt = 0
for row in range(1,6):
    flag = 0
    for col in range(5):
        if apart[0][col] != apart[row][col]:
            flag = 1
            break
    if flag == 0:
        cnt += 1
print(cnt)

def get_sum(nr,nc,m): # (r,c) 부터 n by n 합 구하기
    if nr + m - 1 >= N or nc + m - 1 >= N:
        return int(-21e8)
    sum = 0
    for R in range(m):
        for C in range(m):
            sum += MAP[nr+R][nc+C]
    return sum
MAP = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,2,2,2],
    [1,1,2,2,2],
    [1,1,2,2,2],
]
N = 5
M = 2
max_sum = int(-21e8)
for r in range(N):
    for c in range(N):
        ret = get_sum(r,c,M)
        if ret > max_sum:
            max_sum = ret
print(max_sum)

# 방향배열
MAP = [
    [3,2,1,2],
    [1,2,3,4],
    [5,6,7,8],
    [9,8,7,6]
]
r, c = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(4):
    nr = r + dr[t]
    nc = c + dc[t]
    if nr < 0 or nc < 0 or nr >= 4 or nc >= 4: continue
    if t == 0: print("위")
    if t == 1: print("아래")
    if t == 2: print("왼")
    if t == 3: print("오른")
    print(MAP[nr][nc])
print(MAP[r-1][c+0])
print(MAP[r+1][c+0])
print(MAP[r+0][c-1])
print(MAP[r+0][c+1])
