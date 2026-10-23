class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        fl0, fl1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            fl0, fl1 = fl1, cost[i] + min(fl0, fl1)

        return min(fl0, fl1)

