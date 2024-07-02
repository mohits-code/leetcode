class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d ={}
        for i, n in enumerate(nums):
            c = target - n
            if c in d:
                return[d[c],i]
            d[n]=i
