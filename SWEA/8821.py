T =int(input())
for tc in range(1, T+1):
    word = input()
    paper = []

    for i in range(len(word)):
        if word[i] not in paper:
            paper.append(word[i])
        elif word[i] in paper:
            paper.remove(word[i])

    print(f'#{tc} {len(paper)}')

