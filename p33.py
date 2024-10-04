def searchInRotatedSortedArrayI(nums, target):
    print(f"{nums} -> {target}")
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if target == nums[mid]:
            return mid
        if nums[i] == nums[mid] == nums[j]:
            i += 1
            j -= 1
        elif nums[i] <= nums[mid]:
            if nums[i] <= target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if nums[mid] < target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1


if __name__ == "__main__":

    nums = [
        [2, 5, 6, 0, 0, 1, 2],
        [2, 5, 6, 0, 0, 1],
        [2, 5, 6, 0, 0, 1, 2],
        [1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    ]
    target = [0, 5, 3, 0, 2]
    for i in range(len(nums)):
        print(searchInRotatedSortedArrayI(nums[i], target[i]))
