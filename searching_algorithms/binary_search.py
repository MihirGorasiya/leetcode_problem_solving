def binarySearch(a, target):
    i = 0
    j = len(a) - 1
    while i <= j:
        mid = (i + j) // 2

        if target == a[mid]:
            return mid
        elif target > a[mid]:
            i = mid + 1
        else:
            j = mid - 1

    return -1


if __name__ == "__main__":
    a = [2, 3, 5, 8, 9, 15, 17, 19, 25, 28]
    target = 28
    print(binarySearch(a, target))
