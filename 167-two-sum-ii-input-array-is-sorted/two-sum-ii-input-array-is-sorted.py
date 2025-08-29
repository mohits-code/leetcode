class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        while left<right:
            l=numbers[left]
            r=numbers[right]
            if l+r==target:
                return [left+1, right+1]
            elif l+r>target:
                right-=1
            elif l+r<target:
                left+=1
        