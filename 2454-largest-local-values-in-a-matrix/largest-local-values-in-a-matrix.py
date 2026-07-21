class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        horizontals = [[0] * (n-2) for _ in range(n)]
        for i in range(n):
            for j in range(n-2):
                horizontals[i][j]= max(grid[i][j], grid[i][j+1], grid[i][j+2])
        
        res = [[0] * (n-2) for _ in range((n-2))]
        for x in range(n-2):
            for y in range(n-2):
                res[x][y] = max(horizontals[x][y], horizontals[x+1][y], horizontals[x+2][y])

        return res