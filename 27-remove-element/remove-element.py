class Solution(object):
    def removeElement(self, nums, val):
        
        t=len(nums)

        if val in nums:
            nums.sort()
            i = nums.index(val)
            while nums[i]==val:
                t-=1
                nums.pop(i)
                if i==len(nums):
                    break
        
        return t
        
        
        '''
        total = len(nums)
        for n in nums:
            print(n)
            if n == val:
                total=total-1
                nums.remove(n)


        return total'''