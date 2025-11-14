class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])

        def in_bounds(x, y):
            return 0<=x<n and 0<=y<m
        
        directions=[(0,1), (1,0), (-1,0), (0,-1)]

        q=deque()

        q.append((sr, sc))
        og=image[sr][sc]

        visited=set()

        while q:
            x, y = q.pop()
            
            if (x,y) in visited:
                continue

            image[x][y]=color
            visited.add((x,y))

            for direction in directions:
                nx=x+direction[0]
                ny=y+direction[1]

                if in_bounds(nx,ny):
                    if image[nx][ny]==og:
                        q.append((nx,ny))
        
        return image


