import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = []
        for x, y in points:
            dist = x * x + y * y
            min_heap.append((dist, x, y))        
        heapq.heapify(min_heap)

        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            
        return res
                



