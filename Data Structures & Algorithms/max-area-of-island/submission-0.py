class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        count = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and ((r, c)) not in visited:
                    count = max(count, dfs(r, c))
        return count



