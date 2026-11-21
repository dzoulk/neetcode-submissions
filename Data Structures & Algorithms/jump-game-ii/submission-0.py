class Solution:
    def jump(self, nums: List[int]) -> int:
        jp, cur, end = 0, 0, 0

        for i in range(len(nums) - 1):
            jp = max(jp, i + nums[i])
            if i == end:
                cur += 1
                end = jp

        return cur