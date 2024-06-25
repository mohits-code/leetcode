class Solution(object):
    def removeElement(self, nums, val):
        if val in nums:
            nums.sort()
            i = nums.index(val)
            while i<len(nums) and nums[i]==val:
                nums.pop(i)

        return len(nums)