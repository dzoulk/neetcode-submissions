import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = {}
        for c in tasks:
            if c not in res:
                res[c] = 1
            else:
                res[c] += 1
            
        max_heap = [-count for count in res.values()]
        heapq.heapify(max_heap)

        time, q = 0, deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = -heapq.heappop(max_heap)
                cnt -= 1
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush(max_heap, -cnt)
        return time


        
#my thinking is go through the array, then count every number, if it is not, add it to the hash set, if it is, increment by 1, and then build a max heap based on that, then we check, if they are repeated, then we have to wait n seconds, on the meantime we traverse through the other nodes until n has passed and then we come back to the highest frequency number

