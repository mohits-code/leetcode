class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            if not self.recursive(matrix, i, 0, matrix[i][0]):
                return False

        for j in range(len(matrix[0])):
            if not self.recursive(matrix, 0, j, matrix[0][j]):
                return False 
           
        return True
    
    def recursive(self, matrix, x, y, target):
        if matrix[x][y]!=target:
            return False
        if 0<x+1 and x+1<len(matrix) and 0<y+1 and y+1<len(matrix[0]):
            return self.recursive(matrix, x+1, y+1, target)
        return True
