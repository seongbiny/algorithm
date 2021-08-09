num = int(input())
a = 0
b = 0
cnt = 0

while True:
    a = num//10
    b = num%10
    c = (a+b)%10
    #num = b + c
    #num = (b*10) + c  왜 10을 곱해주지?????????????????
    cnt += 1

    if (num==c):
        break
print(cnt)