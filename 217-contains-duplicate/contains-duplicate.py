class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        uniqueNums=set()

        for num in nums:
            if num in uniqueNums:
                return True
            
            uniqueNums.add(num)
        
        return False
        
        