import sys
input = sys.stdin.readline

def check(num):
    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2
        if card[mid] == num:
            print("1", end=" ")
            break
        elif card[mid] < num:
            start = mid+1
        else:
            end = mid-1
        if start > end:
            print("0", end=" ")
            break

n = int(input())
card = list(input().split())
card.sort()
m = int(input())
check_num = list(input().split())

for i in range(m):
    check(check_num[i])


