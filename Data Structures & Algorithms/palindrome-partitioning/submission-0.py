class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return res
            for j in range(i, len(s)):
                pal = s[i:j+1]
                if pal == pal[::-1]:
                    subset.append(pal)
                    dfs(j + 1)
                    subset.pop()
        dfs(0)
        return res
            

        