import heapq
nums = [1,2]
k = 3
multiplier = 4

res = nums[::]

min_heap = [(n,i) for i,n in enumerate(nums)]
heapq.heapify(min_heap)

for _ in range(k):
    n, i = heapq.heappop(min_heap)
    res[i]*=multiplier
    heapq.heappush(min_heap,(res[i], i))
    
print(res)