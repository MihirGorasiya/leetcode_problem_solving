nums = [3,2,1,5,6,4]
k = 2

res=None

for i in range(len(nums)):
    if res==None:
        res = nums[i]
    if k>0 and nums[i]>res:
        k-=1
    if k==0 and nums[i]>res:
        res = nums[i]
        
print(res)
        