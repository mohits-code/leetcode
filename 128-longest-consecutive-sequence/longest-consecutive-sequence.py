class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet=set(nums)
        maxCount=0
        visited=set()

        for num in nums:
            if num-1 in numSet  or num in visited:
                continue
            currNum=num
            currCount=1
            while currNum+1 in numSet:
                visited.add(currNum)
                currCount+=1
                currNum+=1
            maxCount=max(currCount, maxCount)

        return maxCount

        
        return max(d.values())
        