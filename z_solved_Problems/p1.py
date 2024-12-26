nums = [3, 2, 4]
target = 6
length = len(nums)

for i in range(len(nums)):
    a = 0

    predict_ans = target - nums[i]

    if predict_ans in nums:
        a = nums.index(predict_ans)
        if a == i:
            continue
        break
