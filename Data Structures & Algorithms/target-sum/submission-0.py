class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for x in nums:
            new_dp = defaultdict(int)
            for s, count in dp.items():
                new_dp[s + x] += count
                new_dp[s - x] += count
            dp = new_dp
        
        return dp[target]
