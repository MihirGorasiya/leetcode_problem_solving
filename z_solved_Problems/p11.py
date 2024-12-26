height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
answer = 0
# for i in range(len(height)):
#     for j in range(i+1,len(height)):

#         if height[i] < height[j]:
#             curHeight = height[i]
#         else:
#             curHeight = height[j]
#         tempAns = curHeight * (abs(i-j))

#         if tempAns > answer:
#             answer = tempAns

# print(answer)

i = 0
j = len(height) - 1
answer = 0

while (i < j):
    curHeight = min(height[i], height[j])

    tempAns = curHeight * abs(i-j)

    if tempAns > answer:
        answer = tempAns

    if height[i] > height[j]:
        j -= 1
    else:
        i += 1
print(answer)