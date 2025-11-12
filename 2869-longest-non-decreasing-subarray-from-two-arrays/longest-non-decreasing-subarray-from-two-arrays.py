class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        l=len(nums1)
        dp=[[1 for _ in range(l)] for _ in range(2)]
        max_so_far=1
        for i in range(1,l):
            if nums1[i] >= nums1[i-1]:
                dp[0][i] = max(dp[0][i], dp[0][i-1] + 1)
            if nums1[i] >= nums2[i-1]:
                dp[0][i] = max(dp[0][i], dp[1][i-1] + 1)

            if nums2[i] >= nums1[i-1]:
                dp[1][i] = max(dp[1][i], dp[0][i-1] + 1)
            if nums2[i] >= nums2[i-1]:
                dp[1][i] = max(dp[1][i], dp[1][i-1] + 1)
                
            max_so_far=max(max_so_far,dp[1][i],dp[0][i])
        return max_so_far
        

