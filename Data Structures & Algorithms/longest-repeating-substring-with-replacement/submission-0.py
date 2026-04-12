class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)):
            if s[r] in myDict:
                myDict[s[r]] += 1
            else:
                myDict[s[r]] = 1

            maxf = max(maxf, myDict[s[r]])

            while (r - l + 1) - maxf > k:
                myDict[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
