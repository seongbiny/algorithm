N = int(input())
word = []
for i in range(N):
    j = input()
    if j not in word:
        word.append(j)

# 길이가 짧은 것 -> 길이가 같다면 사전 순

new_word = sorted(word, key=len)
print(new_word)
for i in range(len(new_word)-1, 0, -1):
    if len(new_word[i]) == len(new_word[i-1]):
        if new_word[i][0] < new_word[i-1][0]:
            new_word[i], new_word[i-1] = new_word[i-1], new_word[i]

print(new_word)
