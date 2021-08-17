T = int(input())
pattern = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    n = input()
    lst = list(input().split()) #숫자가 아니니까 map 쓸 필요 없다

    print('f#{tc}', end=' ')
    for p in pattern:
        #lst에서 p랑 같은 것을 출력해라
        for s in lst:
            if p == s:
                print(s, end=' ')
    print()

