matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3


i = 0
j = len(matrix)
n = len(matrix[0]) - 1


def binary_search(a, target):
    print(f"{a} _ {target}")
    i = 0
    j = len(a)

    while i <= j:
        mid = (i + j) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return False


# a = [1, 3, 5, 7]
# print(binary_search(a, 7))
while i < j:
    if matrix[i][n] > target:
        print(f"target: {target}: {binary_search(matrix[i], target)}")
        break
    elif matrix[i][0] == target:
        print(True)
    i += 1
