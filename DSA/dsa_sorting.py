# ----------------------------------- Selection Sorting -----------------------------------

# a = [2, 1, 4, 9, 5, 3, 6, 10]
# a = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
a = [1, 9, 8, 2, 7, 3, 6, 4, 5]

def selSort(array):
    '''
    This is Selection Sort

    In this technique, we keep track of current sorted element
    and the smallest number during current iteration\n
    if smallest number of iteration is smaller than current sorting element\n
    then
    swap both number\n
    and iterate till end of the sort of the array
    '''
    for i in range(0, len(array)-1):
        min = array[i]
        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                array[i], array[j] = array[j], array[i]
    return array
print(selSort(a))


# ----------------------------------- Selection Sorting -----------------------------------

