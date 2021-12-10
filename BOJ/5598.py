word = list(input())

for i in range(len(word)):
    if ord(word[i]) > 67:
        word[i] = chr(ord(word[i])-3)
    else:
        word[i] = chr(ord(word[i])+23)
print(''.join(word))


