class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l=len(nums)
        pre=1
        suf=1
        res=[1]*l
        for i in range(l):
            res[i]*= pre
            pre*=nums[i]

        for j in range(l-1, -1, -1):
            res[j]*=suf
            suf*=nums[j]

        return res
        