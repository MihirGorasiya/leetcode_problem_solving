def jump(nums):
    target = len(nums) - 1
    i = 0
    tempJumpLen = 0
    tempJumpInd = 0
    ans = 0
    while target > 0:
        if target <= nums[i]:
            return ans + 1
        for j in range(1, nums[i] + 1):
            if target - nums[i + j] < target - tempJumpLen:
                tempJumpLen = nums[i + j]
                tempJumpInd = j
            
        target -= tempJumpInd
        i += tempJumpInd
        ans += 1
        tempJumpInd = tempJumpLen = 0
    return ans


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [2, 0, 2, 0, 1]
    # nums = [2, 1]
    # nums = [4, 1, 1, 3, 1, 1, 1]
    # nums = [1, 2, 3]
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
