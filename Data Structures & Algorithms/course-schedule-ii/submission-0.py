class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needs = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            needs[course].append(pre)

        res = []
        visit = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in needs[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
