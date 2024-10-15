def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    less_than_pivot = []
    more_than_pivot = []
    
    for item in arr:
        if item > pivot:
            more_than_pivot.append(item)
        else:
            less_than_pivot.append(item)
    
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)


if __name__ == "__main__":
    a = [10, 16, 8, 12, 15, 6, 3, 9, 5]

    print(f"Quick sort: {quick_sort(a)}")
