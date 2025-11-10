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
            grid[i][j]=0
            area=1
            while q:
                x,y=q.pop()
                for a,b in dirs:
                    nx=x+a
                    ny=y+b
                    if inBounds(nx,ny) and grid[nx][ny] ==1:
                        q.append((nx, ny))
                        grid[nx][ny]=0
                        area+=1
            return area


        maxArea=0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea=max(maxArea,bfs(i,j))

        return maxArea

        
