S = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = []

for i in S:
    word.append(i)

for j in alphabet:
    
    print(word.index(j), end=' ') if j in word else print(-1, end=' ')