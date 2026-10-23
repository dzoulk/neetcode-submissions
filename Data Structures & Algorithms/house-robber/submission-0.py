class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0, 0

        for housevalue in nums:
            temp = max(housevalue + h1, h2)
            h1, h2 = h2, temp

        return h2