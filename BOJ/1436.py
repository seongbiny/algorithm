N = int(input())

# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662 ...

num = 666
cnt = 0
while(True):
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1
