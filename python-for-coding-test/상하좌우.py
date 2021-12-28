n = int(input())
command = list(map(str, input().split()))

arr = [[0] * n for _ in range(n)]

# 1
start_x, start_y = 1, 1
for i in range(len(command)):
    if command[i] == 'R':
        if 1 <= start_x <= n and 1 <= start_y+1 <= n:
            start_y += 1
    elif command[i] == 'L':
        if 1 <= start_x <= n and 1 <= start_y-1 <= n:
            start_y -= 1
    elif command[i] == 'U':
        if 1 <= start_x-1 <= n and 1 <= start_y <= n:
            start_x -= 1
    elif command[i] == 'D':
        if 1 <= start_x+1 <= n and 1 <= start_y <= n:
            start_x += 1

print(start_x, start_y)

