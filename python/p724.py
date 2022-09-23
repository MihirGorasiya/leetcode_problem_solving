from turtle import right


nums = [1, 7, 3, 6, 5, 6]
ans = -1

leftSum = 0
rightSum = 0
numsLength = len(nums)

for i in nums:
    rightSum += i

i = 0
while (i < numsLength):

    rightSum -= nums[i]
    if (leftSum == rightSum and ans == -1):
        ans = i
        break

    leftSum += nums[i]
    i = i+1

print(ans)
