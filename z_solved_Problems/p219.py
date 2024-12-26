nums = [1, 2, 3, 1]
k = 3

window = set()
l = 0

for i in range(len(nums)):
    if len(window) > k:
        window.remove(nums[l])
        l += 1
    if nums[i] in window:
        print("Result found: True")

    window.add(nums[i])

print(False)
