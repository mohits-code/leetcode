class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        all_vals = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        n = len(grid)
        res = [[0] * (n-2) for _ in range((n-2))]

        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = max(grid[x+i+1][y+j+1] for x, y in all_vals)

        return res