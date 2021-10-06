idx = list(input())
# int(ord(idx[0])) - int(ord('a') + 1
col = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
y = col.get(idx[0])
x = int(idx[1])-1
cnt = 0
direction = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

for i, j in direction:
    nx = x + i
    ny = y + j
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)


