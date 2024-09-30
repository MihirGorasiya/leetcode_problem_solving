arr = [3, 2, 1, 56, 10000, 167]
arr = [1, 345, 234, 21, 56789]
arr = [56789]

min = max = arr[0]

i = 0

j = len(arr) - 1
while(i<j):
    if(arr[i]>max or arr[j]>max):
        if(arr[i]>arr[j]):
            max = arr[i]
        else:
            max = arr[j]
    
    if(arr[i] < min or arr[j]<min):
        if(arr[i]<arr[j]):
            min = arr[i]
        else:
            min = arr[j]


    i = i + 1 
    j = j - 1

print(f"Min:{min} __ Max: {max}")