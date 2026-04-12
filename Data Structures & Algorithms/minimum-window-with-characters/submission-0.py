class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        mp = {}
        for ch in t:
            mp[ch] = 1 + mp.get(ch, 0)

        count = len(mp)
        i = 0
        bestlen = float("inf")
        bestpoint = 0

        for j in range(len(s)):
            if s[j] in mp:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count-= 1
                        
            while count == 0:
                windowlen = j - i + 1
                if windowlen < bestlen:
                    bestlen = windowlen
                    bestpoint = i
                
                if s[i] in mp:
                    mp[s[i]] += 1
                    if mp[s[i]] == 1:
                        count+= 1
                i+= 1
        return "" if bestlen == float("inf") else s[bestpoint:bestpoint + bestlen]
            

                
        