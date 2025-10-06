class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        dirs=[(0,1), (1,0), (-1, 0), (0,-1)]
        n=len(grid)

        def inBounds(x, y):
            return 0<=x<n and 0<=y<n

        pq=[]
        heapq.heappush(pq,(grid[0][0],0,0))

        currMax=0

        visited=set()

        while pq:
            curr, x, y = heapq.heappop(pq)

            visited.add(curr)

            if curr>currMax:
                currMax=curr
            
            if x==n-1 and y==n-1:
                return currMax
            
            for d in dirs:
                nx=x+d[0]
                ny=y+d[1]
                if inBounds(nx,ny):
                    if grid[nx][ny] not in visited:
                        heapq.heappush(pq,(grid[nx][ny],nx,ny))
        
        return currMax