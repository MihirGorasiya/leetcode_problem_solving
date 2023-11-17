# hours = [0, 1, 2, 3, 4]
hours = [5,1,4,2,2]
# target = 2
target = 6

counter = 0
for i in hours:
    if i >= target:
        counter = counter + 1
    
print(counter)