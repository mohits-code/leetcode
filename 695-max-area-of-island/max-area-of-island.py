class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        def inBounds(x,y):
            return 0<=x<n and 0<=y<m
        
        dirs=[(0,-1), (-1,0), (0,1), (1,0)]

        def bfs(i,j):
            q=deque()
            q.append((i,j))
            area=0
            while q:
                x,y=q.pop()
                if grid[x][y]==0:
                    continue
                grid[x][y]=0
                area+=1
                for a,b in dirs:
                    if inBounds(x+a,y+b):
                        if grid[x+a][y+b] ==1:
                            q.append((x+a, y+b))
            return area


        maxArea=0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea=max(maxArea,bfs(i,j))

        return maxArea

        
