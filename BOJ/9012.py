t = int(input())
for tc in range(t):
    vps = list(input())

    stack = []
    for i in range(len(vps)):
        if len(stack) == 0:
            stack.append(vps[i])
        elif stack[-1] == '(' and vps[i] == '(':
            stack.append(vps[i])
        elif stack[-1] == '(' and vps[i] == ')':
            stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')