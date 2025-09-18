class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        comps=dict()
        l=len(nums)
        for i in range(l):
            curr = nums[i]
            if curr in comps:
                return [comps[curr], i]
            comps[target-curr]=i

        