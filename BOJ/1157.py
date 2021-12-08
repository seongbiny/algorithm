lst = [0]*26

word = str(input())

for i in word:
    if i == 'a' or i == 'A':
        lst[0] += 1
    elif i == 'b' or i == 'B':
        lst[1] += 1
    elif i == 'c' or i == 'C':
        lst[2] += 1
    elif i == 'd' or i == 'D':
        lst[3] += 1
    elif i == 'e' or i == 'E':
        lst[4] += 1
    elif i == 'f' or i == 'F':
        lst[5] += 1
    elif i == 'g' or i == 'G':
        lst[6] += 1
    elif i == 'h' or i == 'H':
        lst[7] += 1
    elif i == 'i' or i == 'I':
        lst[8] += 1
    elif i == 'j' or i == 'J':
        lst[9] += 1
    elif i == 'k' or i == 'K':
        lst[10] += 1
    elif i == 'l' or i == 'L':
        lst[11] += 1
    elif i == 'm' or i == 'M':
        lst[12] += 1
    elif i == 'n' or i == 'N':
        lst[13] += 1
    elif i == 'o' or i == 'O':
        lst[14] += 1
    elif i == 'p' or i == 'P':
        lst[15] += 1
    elif i == 'q' or i == 'Q':
        lst[16] += 1
    elif i == 'r' or i == 'R':
        lst[17] += 1
    elif i == 's' or i == 'S':
        lst[18] += 1
    elif i == 't' or i == 'T':
        lst[19] += 1
    elif i == 'u' or i == 'U':
        lst[20] += 1
    elif i == 'v' or i == 'V':
        lst[21] += 1
    elif i == 'w' or i == 'W':
        lst[22] += 1
    elif i == 'x' or i == 'X':
        lst[23] += 1
    elif i == 'y' or i == 'Y':
        lst[24] += 1
    elif i == 'z' or i == 'Z':
        lst[25] += 1

maxV = max(lst)
if lst.count(maxV) > 1:
    print('?')
else:
    idx = lst.index(maxV)
    print(chr(idx+65))