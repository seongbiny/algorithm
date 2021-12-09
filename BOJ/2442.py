n = int(input())           # 4 3 2 1 0
for i in range(1, 2*n, 2): # 1 3 5 7 9
    print(' '*(((2*n)-1-i)//2)+'*'*i)

