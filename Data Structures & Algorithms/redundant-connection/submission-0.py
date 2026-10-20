class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = {i: [] for i in range(n + 1)}
     
        def dfs(node, target, visit):
            if node == target:
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True
            return False

        for a, b in edges:
            if dfs(a, b, set()):
                return [a, b]
            adj[a].append(b)
            adj[b].append(a)
            
