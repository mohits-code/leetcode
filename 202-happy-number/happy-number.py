class Solution:
    def isHappy(self, n: int) -> bool:
        nums=set()

        while n != 1:
            copy=n
            curr=0
            while copy>0:
                curr+=(copy%10)**2
                copy//=10
            if curr in nums:
                return False
            nums.add(curr)
            n=curr
        
        return True
