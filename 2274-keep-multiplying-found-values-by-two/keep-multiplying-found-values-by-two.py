class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==original:
                original*=2
                r=len(nums)-1
            elif nums[mid]<original:
                l=mid+1
            else:
                r=mid-1
        return original
            
