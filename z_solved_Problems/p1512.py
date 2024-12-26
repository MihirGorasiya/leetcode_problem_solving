# nums = [1, 2, 3, 1, 1, 3]
# nums = [1,1,1,1]
nums = [1,2,3]

i = 0
j = len(nums)-1


answer = 0

while i < j:
    if nums[i] == nums[j]:
        answer = answer + 1
                
    if j-1 == i:
        j = len(nums)-1
        i += 1
    else:
        j -= 1

print(answer)
