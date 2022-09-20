nums = [1, 1, 1, 1, 1]


class Solution(object):
    def runningSum(self, nums):


        ans = []

        k = 0
        i = 0

        while (i < len(nums)):
            k = k+nums[i]
            ans.append(k)
            i = i+1

        return ans

