n = int(input())
score = list(map(int, input().split()))

middle = round(sum(score) / len(score))

minV = 9999999999
num = 0
for i in range(n):
    if middle > score[i]:
        if middle-score[i] <= minV and num > i:
            minV = middle-score[i]
            num = i+1
    if middle <= score[i]:
        if score[i]-middle <= minV and num > i:
            minV = score[i]-middle
            num = i+1


print(middle, num)

# 틀림