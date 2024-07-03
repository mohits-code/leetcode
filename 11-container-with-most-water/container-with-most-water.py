class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        l=0
        r=len(height)-1
        while(l<r):
            x=(r-l)*min(height[l],height[r])
            if x>m:
                m=x
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return m