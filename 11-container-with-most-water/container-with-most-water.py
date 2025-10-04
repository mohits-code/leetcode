class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left = 0
        right=n-1
        total=0
        while left<right:
            curr=min(height[left],height[right])*(right-left)
            if curr>total:
                total=curr
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return total