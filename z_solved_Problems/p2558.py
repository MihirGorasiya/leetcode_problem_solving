import heapq
import math
gifts = [25, 64, 9, 4, 100]
k = 4

gifts = [-g for g in gifts]
heapq.heapify(gifts)

for _ in range(k):
    n = -heapq.heappop(gifts)
    heapq.heappush(gifts, math.floor(math.sqrt(n)))


print(-sum(gifts))
