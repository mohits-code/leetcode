class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        comps=dict()

        for i in range(len(nums)):
            val=nums[i]
            if val in comps:
                return [comps[val],i]
            comps[target-val]=i
        
        