import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    word = list(map(str, input().split()))
    if word[0] == 'push':
        stack.append(word[1])
    elif word[0] == 'pop':
        if len(stack) != 0:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)