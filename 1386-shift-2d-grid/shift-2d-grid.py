class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (n*m)

        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = grid[(i + (j - k) // n) % m][(j - k) % n]        
        return res