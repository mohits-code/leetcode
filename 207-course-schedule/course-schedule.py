class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        courseDict=defaultdict(list)


        for course,req in prerequisites:
            courseDict[req].append(course)

        
        visited=set()
        visiting=set()

        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(courseDict, i, visited, visiting):
                    return False

        return True
        
    
    def dfs(self, courseDict, curr, visited, visiting):
        if curr in visited:
            return True

        if curr in visiting:
            return False

        visiting.add(curr)

        for course in courseDict[curr]:
            if not self.dfs(courseDict, course, visited, visiting):
                return False
        
        visited.add(curr)
        visiting.remove(curr)
        return True



        