class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carTime = []
        for car in range(len(position)):
            time = (target - position[car]) / speed[car]
            carTime.append((position[car], time))

        carTime.sort(reverse=True)

        stack = []

        for position, time in carTime:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)