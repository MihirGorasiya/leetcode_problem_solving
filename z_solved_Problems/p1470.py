nums = [2,5,1,3,4,7]
ans = [0]*nums.__len__()
n = 3

for i in range(0, n):
    ans[i*2] = nums[i]
    ans[(i*2)+1] = nums[i+n]

print(ans)