class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            new_list = []
            for p in res:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_list.append(p_copy)
            res = new_list
        return new_list

            