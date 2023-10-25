nums = [-1, 2, 1, -4]
target = 1

answer = float('inf')
nums.sort()

for i in range(len(nums)-2):
    l = i+1
    r = len(nums)-2
    while (l < r):
        sum = nums[i] + nums[l]+nums[r]

        diff = abs(target-sum)

        if diff < answer:
            answer=diff
        
        if sum<target:
            l+=1
        else:
            r-=1

print(answer)