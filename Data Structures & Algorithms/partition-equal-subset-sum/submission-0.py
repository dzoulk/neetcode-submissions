class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for t in range(target, x - 1, -1):
                dp[t] = max(dp[t], dp[t-x])

        return dp[target]

          


