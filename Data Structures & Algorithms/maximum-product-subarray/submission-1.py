class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, minVal, maxVal = nums[0], 1, 1

        for val in nums:
            maxVal, minVal = max(val * maxVal, val * minVal, val), min(val * maxVal, val * minVal, val)
            res = max(res, maxVal)

        return res