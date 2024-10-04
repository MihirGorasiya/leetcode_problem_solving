def binarySearch(nums, target):
    i, j = 0, len(nums) - 1

    while i <= j:
        mid = (i + j) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            i = mid + 1
        else:
            j = mid - 1
    return -1


if __name__ == "__main__":

    nums = [[-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]]
    target = [9, 2]

    for i in range(len(nums)):
        print(binarySearch(nums[i], target[i]))
