class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            taken[course].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if taken[course] == []:
                return True
            
            visit.add(course)
            for pre in taken[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            taken[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            