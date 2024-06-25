class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums1=nums1+nums2
        nums1.sort()
        return median(nums1)
        
def median (nums):
    l = len(nums)
    if l%2==1:
        return nums[l//2]
    if l is 0:
        return 0
    return (nums[l//2]+nums[l//2-1])/2.0

    