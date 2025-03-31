import heapq


A = [2, 3, 10, 5, 4, 0]
HEAP = []

for i in range(len(A)):
    heapq.heappush(HEAP, (A[i], i))

print([heapq.heappop(HEAP)[1] for _ in range(2)])
