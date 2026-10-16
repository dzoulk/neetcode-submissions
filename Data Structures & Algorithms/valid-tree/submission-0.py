from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set([0])
        q = deque([(0, -1)])

        while q:
            node, parent = q.popleft()
            for val in adj[node]:
                if val == parent:
                    continue
                if val in visit:
                    return False
                visit.add(val)
                q.append((val, node))

        return len(visit) == n