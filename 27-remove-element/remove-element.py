class Solution(object):
    def removeElement(self, nums, val):
        

        if val in nums:
            nums.sort()
            i = nums.index(val)
            while nums[i]==val:
                nums.pop(i)
                if i==len(nums):
                    break
        
        return len(nums)
        