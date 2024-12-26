# Kids With the Greatest Number of Candies

candies = [2,3,5,1,3]
extraCandies = 3

a = []
ma = max(candies)

for i in candies:
    if i + extraCandies >= ma:
        a.append(True)
    else:
        a.append(False)

print(a)