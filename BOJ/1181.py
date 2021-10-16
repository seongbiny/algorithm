N = int(input())
words = set()
for _ in range(N):
    word = input()
    words.add((word, len(word)))

# 길이가 짧은 것 -> 길이가 같다면 사전 순

new_word = sorted(words, key=lambda x:(x[1], x[0]))

for i in new_word:
    print(i[0])

