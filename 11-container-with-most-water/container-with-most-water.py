class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        l=0
        r=len(height)-1
        h=max(height)
        while(l<r):
            if height[l] >= height[r]:
                temp = (r-l)*height[r]
                r-=1
            else:
                temp = (r-l)*height[l]
                l+=1
            m=max(m, temp)
            if m>=h*(r-l):
                break
        return m