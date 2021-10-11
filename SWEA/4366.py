T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    trinary = list(input())
    bi_lst = []
    tri_lst = []

    for i in range(len(binary)):
        bi_change = binary.copy()
        if bi_change[i] == '0':
            bi_change[i] = '1'
            bi_lst.append(int(''.join(bi_change), 2))
        else:
            bi_change[i] = '0'
            bi_lst.append(int(''.join(bi_change), 2))

    for i in range(len(trinary)):
        tri_change = trinary.copy()
        if tri_change[i] == '0':
            tri_change[i] = '1'
            tri_lst.append(int(''.join(tri_change), 3))
            tri_change[i] = '0'
            tri_change[i] = '2'
            tri_lst.append(int(''.join(tri_change), 3))
        elif tri_change[i] == '1':
            tri_change[i] = '2'
            tri_lst.append(int(''.join(tri_change), 3))
            tri_change[i] = '1'
            tri_change[i] = '0'
            tri_lst.append(int(''.join(tri_change), 3))
        else:
            tri_change[i] = '0'
            tri_lst.append(int(''.join(tri_change), 3))
            tri_change[i] = '2'
            tri_change[i] = '1'
            tri_lst.append(int(''.join(tri_change), 3))
    #print(bi_lst, tri_lst)
    for i in bi_lst:
        for j in tri_lst:
            if i == j:
                print(f'#{tc} {i}')
                break








