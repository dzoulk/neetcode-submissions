class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True

        for i in range(n - 1, -1, -1):
            for open in range(n):
                if s[i] == '*':
                    as_open = dp[i + 1][open + 1]
                    as_close = open > 0 and dp[i + 1][open - 1]
                    as_empty = dp[i + 1][open]
                    dp[i][open] = as_open or as_close or as_empty
                elif s[i] == '(':
                    dp[i][open] = dp[i + 1][open + 1]
                else:
                    dp[i][open] = open > 0 and dp[i + 1][open - 1]

        return dp[0][0]