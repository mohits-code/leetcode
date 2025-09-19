class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l=len(numbers)

        left=0
        right=l-1

        while left<right:
            currTarget = numbers[left] + numbers[right]
            if currTarget == target:
                return [left+1, right+1]
            elif currTarget > target:
                right-=1
            else:
                left+=1