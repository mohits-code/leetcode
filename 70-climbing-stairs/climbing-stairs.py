class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        prev=3
        curr=2
        total=5
        for i in range(4,n):
            curr=prev
            prev=total
            total+=curr
        return total