class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1=nums1+nums2
        nums1.sort()
        return median(nums1)
        
def median (n):
    l = len(n)
    if l%2==1:
        return n[l//2]
    if l is 0:
        return 0
    return (n[l//2]+n[l//2-1])/2.0
