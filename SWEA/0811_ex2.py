import sys
sys.stdin = open("in2.txt","r")

T = int(input())
for tc in range(1, T+1):

    arr = list(map(int,input().split()))
    n = len(arr)

    for i in range(1<<n):
        sumV = 0
        for j in range(n):
            r = i & (1<<j)
            if r != 0:
                sumV += arr[j]
                if sumV == 0:
                    print('True')
                    break