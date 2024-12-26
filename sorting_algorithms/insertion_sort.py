def insertion_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        key = a[i]
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = key

    return a


if __name__ == "__main__":
    a = [2, 5, 3, 8, 4, 1, 9, 6]
    print(a)
    print(insertion_sort(a))
