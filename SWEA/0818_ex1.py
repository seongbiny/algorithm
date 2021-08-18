def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return -1
    else:
        return s.pop(-1)

s = []
push(1)
push(2)
push(3)
push(4)
push(4)
print(pop()) # result = pop()
print(pop())
print(pop())
print(s)