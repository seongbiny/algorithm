word = input()
call = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in word:
    idx = 0
    for j in range(len(call)):
        if i in call[j]:
            idx = j

    time += idx+3

print(time)
