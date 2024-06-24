class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1=nums1+nums2
        nums1.sort()
        return median(nums1)






'''if len(nums1) is 0:
            return median(nums2)
        if len(nums2) is 0:
            return median(nums1) 
        return median([median(nums1),median(nums2)])
'''
def median (nums):
    l = len(nums)
    if l is 0:
        return 0
    if l%2==1:
        return nums[l//2]
    return (nums[l//2]+nums[l//2-1])/2.0