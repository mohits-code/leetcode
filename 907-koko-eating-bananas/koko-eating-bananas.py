class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
        curr=r
        while l<=r:
            mid = (l + r) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            
            if total_hours <= h:
                curr = mid
                r = mid - 1
            else:
                l = mid + 1
        return curr