class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = {}
        for ch in s1:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1

        count = len(mp)
        i = 0
        k = len(s1)
        for j in range(len(s2)):
            if s2[j] in mp:
                mp[s2[j]] -= 1
                if mp[s2[j]] == 0:
                    count -= 1
            if j - i + 1 == k:
                if count == 0:
                    return True

                if s2[i] in mp:
                    mp[s2[i]] += 1
                    if mp[s2[i]] == 1:
                        count += 1
                i += 1

        return False
