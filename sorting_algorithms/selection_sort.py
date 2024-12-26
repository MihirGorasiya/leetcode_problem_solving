def selection_sort(a):

    n = len(a)

    for i in range(n):
        smallest = i
        for j in range(i, n):
            if a[smallest] > a[j]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]

    return a


if __name__ == "__main__":
    a = [2, 5, 3, 8, 4, 1, 9, 6]
    print(a)
    print(selection_sort(a))
