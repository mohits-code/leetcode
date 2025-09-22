class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height)<=1:
            return 0

        l=len(height)
        mostWater=0

        left=0
        right=l-1

        while left<right:
            leftVal=height[left]
            rightVal=height[right]

            currWater=min(leftVal, rightVal)*(right-left)

            if currWater > mostWater:
                mostWater = currWater

            if rightVal>leftVal:
                left+=1
            else:
                right-=1        

        return mostWater

        