class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        lp=len(potions)
        for i in range(len(spells)):
            l=0
            r=lp-1
            m=lp
            while l<=r:
                mid=l+(r-l)//2
                if spells[i]*potions[mid]>=success:
                    r=mid-1
                    m=mid
                else:
                    l=mid+1
                
            res.append(lp-m)
        return res