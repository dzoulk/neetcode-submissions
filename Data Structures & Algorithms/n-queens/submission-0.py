class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag = set()
        negDiag = set()
        board = []
        for _ in range(n):
            board.append(["."] * n)

        def dfs(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in diag or (r - c) in negDiag:
                    continue
                cols.add(c)
                diag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                cols.remove(c)
                diag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res