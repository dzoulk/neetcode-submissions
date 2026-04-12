class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        part = set(nums)
        for num in nums:
            if (num - 1) not in part:
                length = 0
                while (num + length) in part:
                    length+=1
                longest = max(length, longest)

        return longest