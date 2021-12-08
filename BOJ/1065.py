def hansu(num):
    if len(str(num)) == 1:
        return True
    elif len(str(num)) == 2:
        return True
    elif len(str(num)) == 3:
        if (num//100 - (num//10)%10) == ((num//10)%10 - num%10):
            return True

n = int(input())
cnt = 0
for i in range(1, n+1):
    if hansu(i) == True:
        cnt += 1

print(cnt)