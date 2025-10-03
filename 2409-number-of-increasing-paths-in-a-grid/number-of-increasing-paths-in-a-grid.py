class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dirs=[(-1,0),(0,-1),(1,0),(0,1)]
        mod=10**9+7
        dp=[m*[0] for _ in range(n)]
        
        def inBounds(x, y):
            return 0<=x<n and 0<=y<m

        def dfs(x, y):
            if dp[x][y]!=0:
                return dp[x][y]

            count=1

            for d in dirs:
                nx = x+d[0]
                ny = y+d[1]
                if inBounds(nx, ny):
                    if grid[nx][ny]>grid[x][y]:
                        count=(count+dfs(nx,ny))%mod
            
            dp[x][y]=count

            return count
        
        total=0
        for i in range(n):
            for j in range(m):
                total=(total+dfs(i,j))%mod
        return total