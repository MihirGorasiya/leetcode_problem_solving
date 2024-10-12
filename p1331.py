arr = [40, 10, 20, 30]
arr = [40, 10, 20, 30]
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]

tempArr = arr.copy()
tempArr.sort()
# for rank, num in enumerate(tempArr):
#     print(f'{num:rank+1}')
# rank_map = {num: rank + 1 for rank, num in enumerate(tempArr)}


print({num: rank + 1 for rank, num in enumerate(tempArr)})
