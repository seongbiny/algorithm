T = int(input())

scores = list(map(int,input().split()))
new_scores = []
M = max(scores)
for j in scores:
    new_scores.append(j/M*100)

print(sum(new_scores)/len(new_scores))