class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        my_list = []

        def dfs(open, close):
            if open == close == n:
                res.append("".join(my_list))
                return
            if open < n:
                my_list.append("(")
                dfs(open + 1, close)
                my_list.pop()
            if close < open:
                my_list.append(")")
                dfs(open, close + 1)
                my_list.pop()
        dfs(0, 0)
        return res


        