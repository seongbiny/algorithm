N = int(input())
# lst = []
# for i in range(N):
#     name, score = input().split()
#     lst.append([score, name])
# result = sorted(lst)
#
# for i in range(len(result)):
#     print(result[i][1], end=' ')

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
