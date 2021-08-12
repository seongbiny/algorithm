import sys
sys.stdin = open("input_ladder.txt","r")

T = 10

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            result = i

    row, col = 99, i

    while row != 0:
        row -= 1
        if col == 0:



