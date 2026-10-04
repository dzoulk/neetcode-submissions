class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dig = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return res
        def dfs(i):
            if i == len(digits):
                res.append("".join(dig))
                return 
            for c in digitToChar[digits[i]]:
                dig.append(c)
                dfs(i+1)
                dig.pop()

        dfs(0)
        return res
            
                
                
