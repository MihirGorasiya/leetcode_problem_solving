nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

# nums1 = [3,1]
# nums2 = [2,3]
# nums3 = [1,2]

# nums1 = [1,2,2]
# nums2 = [4,3,3]
# nums3 = [5]


res = []

seen1 = set(nums1)
seen2 = set(nums2)
seen3 = set(nums3)

for i in seen1:
    
    if i in seen2 and i in seen3:
        res.append(i)
        seen2.remove(i)
        seen3.remove(i)
        
    if i in seen2:
        res.append(i)
        seen2.remove(i)
        continue
    if i in seen3:
        res.append(i)
        seen3.remove(i)

for i in seen2:
    if i in seen1:
        res.append(i)
        seen1.remove(i)
        continue
    if i in seen3:
        res.append(i)
        seen3.remove(i)

for i in seen3:
    if i in seen2:
        res.append(i)
        seen2.remove(i)
        continue
    if i in seen1:
        res.append(i)
        seen1.remove(i)


print( res)
    