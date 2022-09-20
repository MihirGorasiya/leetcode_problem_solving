nums = [2, 7, 11, 15]
target = 9
answer = [0,0]

for x in nums:
    for y in nums:
        if (x+y == target):
            answer[0] = nums.index(y)
            answer[1] = nums.index(x)

print(answer)
