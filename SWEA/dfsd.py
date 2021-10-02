n = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,
    '0110001':5,'0101111':6, '0111011':7,'0110111':8,'0001011':9}
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    code = [input() for _ in range(N)]
    found = False
    for i in range(N):
        for j in range(M-1,-1,-1):
            if code[i][j] == '1':
                r_idx = i
                c_idx = j
                found = True
                break
        if found:
            break
    newcode = code[r_idx][c_idx-55:c_idx+1]
    even,odd = 0,0
    for k in range(7):
        if k%2==0:
            even += n[newcode[7*k:7*(k+1)]]
        else:
            odd += n[newcode[7*k:7*(k+1)]]
    r = even*3 + odd
    if (r+n[newcode[-7:]])%10 != 0:
        r = 0
    else:
        r = even+odd+n[newcode[-7:]]
    print(f"#{tc} {r}")