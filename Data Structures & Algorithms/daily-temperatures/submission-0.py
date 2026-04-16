class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        for d in range(len(temperatures)):
            while stack and temperatures[d] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = d - prev

            stack.append(d)
        return res  