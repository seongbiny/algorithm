T = int(input())

for i in range(1,T+1):
    word = input()
    a = list(word)
    result = []

    for j in range(len(a)//2):
        if a[j] == a[-1-j]:
            result.append(1)
        else:
            result.append(0)
    
    if all(result):
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')