class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        n=len(matrix)
        m=len(matrix[0])

        l=0
        r=m*n-1

        while l<=r:
            mid=(l+r)//2
            mid_r=mid//m
            mid_c=mid%m
            mid_val=matrix[mid_r][mid_c]
            if mid_val==target:
                return True
            elif mid_val>target:
                r=mid-1
            else:
                l=mid+1
        
        return False