class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        d = l*[1]
        left=1
        for i in range(l):
            d[i]*=left
            left*=nums[i]
        right=1
        for j in reversed(range(l)):
            d[j]*=right
            right*=nums[j]
        return d
        