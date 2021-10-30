from itertools import combinations

L, C = map(int, input().split())
lst = list(map(str, input().split()))

combi = list(combinations(lst, 4))
combi.sort()

for i in combi:
    password = ''
    vowel, consonant = 0, 0
    for j in range(len(i)):
        if i[j] in 'aeiou':
            vowel += 1
        else:
            consonant += 1
        password += i[j]
        if vowel >= 1 and consonant >= 2:
            print(password)