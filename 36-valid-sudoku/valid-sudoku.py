class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=defaultdict(set)
        cols=defaultdict(set)
        boxes=defaultdict(set)
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val !=".":
                    ix=(i//3)*3+(j//3)
                    if val in rows[i] or val in cols[j] or val in boxes[ix]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[ix].add(val)
        return True




        