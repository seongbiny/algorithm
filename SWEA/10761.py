T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())

    b_pos, o_pos = 1, 1
    b_time, o_time = 0, 0

    for i in range(1, len(lst), 2):
        goal = int(lst[i+1])
        if lst[i] == 'B':
            b_pos += 1
            b_time += 1
            if lst[i+1] == b_pos:
                b_time += 1

        elif lst[i] == 'O':
            pass

