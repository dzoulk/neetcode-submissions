class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jp = 0

        for i in range(len(nums)):
            if i > jp:
                return False
            jp = max(jp, i + nums[i])

        return True