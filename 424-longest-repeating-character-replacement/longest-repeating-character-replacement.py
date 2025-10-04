class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=defaultdict(int)
        left=total=curr=0
        for right in range(len(s)):
            d[s[right]]+=1
            curr=max(curr,d[s[right]])
            if (right-left+1)-curr>k:
                d[s[left]]-=1
                left+=1
            total=max(total,right-left+1)
        return total


                    