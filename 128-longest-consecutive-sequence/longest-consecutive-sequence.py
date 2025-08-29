class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=set(nums)
        mc=0
        for num in x:
            if num-1 not in x:
                c=1
                while num+c in x:
                    c+=1
                mc=max(mc,c)
        return mc
        