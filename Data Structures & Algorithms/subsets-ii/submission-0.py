class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                start = 0
            
            size = len(res)
            new_subset = []
            for subset in res[start:]:
                new_subset.append(subset + [nums[i]])
            res += new_subset
            start = size
        return res
