import sys
input = sys.stdin.readline

n = int(input())
deque = []
for i in range(n):
    word = list(map(str, input().split()))
    if word[0] == 'push_front':
        deque.insert(0, word[1])
    elif word[0] == 'push_back':
        deque.append(word[1])
    elif word[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif word[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif word[0] == 'size':
        print(len(deque))
    elif word[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif word[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])