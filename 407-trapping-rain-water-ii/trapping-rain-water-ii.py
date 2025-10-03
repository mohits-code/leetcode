class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        n=len(heightMap)
        m=len(heightMap[0])
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]

        def inBounds(x,y):
            return 0<=x<n and 0<=y<m

        pq=[]
        visited=set()
        for i in range(n):
            heapq.heappush(pq, (heightMap[i][0],i,0))
            heapq.heappush(pq, (heightMap[i][m-1],i,m-1))
            visited.add((i,0))
            visited.add((i,m-1))
        for j in range(1,m-1):
            heapq.heappush(pq, (heightMap[0][j],0,j))
            heapq.heappush(pq, (heightMap[n-1][j],n-1,j))
            visited.add((0,j))
            visited.add((n-1,j))

        total=0
        while pq:
            curr=heapq.heappop(pq)
            for d in dirs:
                nx=curr[1]+d[0]
                ny=curr[2]+d[1]
                if inBounds(nx,ny) and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    total+=max(0,curr[0]-heightMap[nx][ny])

                    nh=max(curr[0],heightMap[nx][ny])
                    heapq.heappush(pq,(nh,nx,ny))
        return total
                    

