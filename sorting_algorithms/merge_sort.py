def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2

        left_half = a[:mid]
        right_half = a[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1
    return a


if __name__ == "__main__":
    a = [2, 5, 3, 8, 4, 1, 9, 6]
    print(a)
    print(merge_sort(a))
