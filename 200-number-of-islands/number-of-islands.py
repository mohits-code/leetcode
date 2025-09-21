class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islandCount=0

        m=len(grid)
        n=len(grid[0])

        visited=set()

        for i in range(m):
            for j in range(n):
                if (i,j) in visited or grid[i][j]=="0":
                    continue
                self.bfs(grid, i, j, visited)
                islandCount+=1

        return islandCount



    def bfs(self, grid, i, j, visited):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        
        if grid[i][j]=="0" or (i,j) in visited:
            return
        
        visited.add((i,j))

        self.bfs(grid, i-1, j, visited)
        self.bfs(grid, i+1, j, visited)
        self.bfs(grid, i, j-1, visited)
        self.bfs(grid, i, j+1, visited)


        