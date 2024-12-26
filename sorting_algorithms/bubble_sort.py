def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


if __name__ == "__main__":
    a = [2, 5, 3, 8, 4, 1, 9]
    a = [2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
    print(bubble_sort(a))
