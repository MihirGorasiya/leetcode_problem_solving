nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# nums1 = [0, 0, 0, 0, 0]
# m = 0
# nums2 = [1, 2, 3, 4, 5]
# n= 5
    
i = m - 1
j = n - 1
k = m + n - 1
    
    
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
    
    
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(nums1)
