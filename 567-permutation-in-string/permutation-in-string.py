class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in range(len(s1)):
            d1[s1[i]]+=1
            d2[s2[i]]+=1

        if d1 == d2:
            return True

        c=0
        for j in range(len(s1), len(s2)):
            d2[s2[j]]+=1
            d2[s2[c]]-=1
            if d2[s2[c]]==0:
                del d2[s2[c]]
            c+=1
            if d1==d2:
                return True

        return False