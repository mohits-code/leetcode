class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return 

        l=len(nums)
        nums.sort()

        res=[]

        for i in range(l-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue 
                
            target = 0-nums[i]

            left = i+1
            right = l-1

            while left<right:
                curr = nums[left]+nums[right]

                if curr<target:
                    left+=1
                elif curr>target:
                    right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        
        return res