class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r,c)]
            best = 1
            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))
            dp[(r,c)] = best
            return best

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res
##Get rows and cols, and make dp = {}. Write dfs(r, c): if (r, c) is in dp, return the saved value start best = 1 for each of the 4 directions: if the neighbor is in bounds and bigger, set best = max(best, 1 + dfs(nr, nc)) save dp[(r, c)] = best and return it Loop over every cell, call dfs, and return the largest result.