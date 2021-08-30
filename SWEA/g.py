s = 'ATCKB'
arr = [[s] for _ in range(5)]
i = 0
arr1 = [[s] for _ in range(len(arr)) if len(arr) >= 0]
print(arr)
print(arr1)