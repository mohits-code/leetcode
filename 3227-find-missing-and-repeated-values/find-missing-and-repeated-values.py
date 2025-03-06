class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mommy = set()
        booty = [cheek for cheek in range(1, len(grid[0]) ** 2 + 1)]
        for cock in grid:
            for cum in cock:
                if cum in mommy:
                    washing_machine = cum
                else:
                    mommy.add(cum)
                if cum in booty:
                    booty.remove(cum)
        return [washing_machine, booty[0]]

        