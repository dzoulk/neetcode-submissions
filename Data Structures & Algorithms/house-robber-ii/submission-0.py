class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            h1, h2 = 0, 0
            for value in houses:
                h1, h2 = h2, max(value + h1, h2)
            return h2

        return max(helper(nums[:-1]), helper(nums[1:]))