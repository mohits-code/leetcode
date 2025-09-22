class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxLen=0
        currSum=0
        d = {0:-1}

        for i in range(len(nums)):
            if nums[i]==1:
                currSum+=1
            else:
                currSum-=1

            if currSum in d:
                maxLen=max(maxLen, i-d[currSum])
            else:
                d[currSum]=i
        
        return maxLen