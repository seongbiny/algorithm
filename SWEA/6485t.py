T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append(a)
        arr.append(b)

    p = int(input())
    for i in range(p):
        c = int(input())

    adj_list = [[] for _ in range(p+1)]
    for i in range(n):
        adj_list[arr[2*i]].append(arr[2*i+1])


