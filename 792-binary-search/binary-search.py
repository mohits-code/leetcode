class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n=len(nums)
        
        l=0
        r=n-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
           
        return -1
