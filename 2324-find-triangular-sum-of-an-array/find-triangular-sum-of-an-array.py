class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res=0
        l=len(nums)
        for i in range(l):
            res+=nums[i]*math.comb(l-1, i)
        return res%10