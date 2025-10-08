class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for i in range(len(spells)):
            l=0
            r=len(potions)-1
            m=len(potions)
            while l<=r:
                mid=l+(r-l)//2
                if spells[i]*potions[mid]>=success:
                    r=mid-1
                    m=mid
                else:
                    l=mid+1
                
            res.append(len(potions)-m)
        return res