nums = [0, 1, 2, 4, 5, 7]
nums = [0,2,3,4,6,8,9]
nums.index(3)
startNumber = None
lastNumber = None
ans = []
for i in nums:
    print(f"\n{i} _ {startNumber} _ {lastNumber}")
    if lastNumber != None and i == lastNumber + 1:
        print("if")
        lastNumber = i
    elif lastNumber == None and startNumber != None and i == startNumber + 1:
        print("elif")
        lastNumber = i
    elif lastNumber == None and startNumber != None and i > startNumber + 1:
        print("elif 2")
        ans.append(f"{startNumber}")
        startNumber = i
    else:
        print("else")
        if startNumber != None:
            ans.append(f"{startNumber}->{lastNumber}")
            startNumber = lastNumber = None
        startNumber = i

if lastNumber == None and startNumber != None:
    ans.append(f"{startNumber}")
else:
    ans.append(f"{startNumber}->{lastNumber}")

print(ans)
