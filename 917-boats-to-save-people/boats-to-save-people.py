class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        people.sort()
        r=len(people)-1
        l=0

        while l<=r:
            if people[r]+people[l]<=limit:
                l+=1
            r-=1
            res+=1

        return res

