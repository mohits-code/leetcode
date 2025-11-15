class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx=len(s)-1

        while idx>=0:
            if s[idx]==" ":
                idx-=1
            else:
                break
        
        count=0
        while idx>=0:
            if s[idx]!=" ":
                count+=1
                idx-=1
            else:
                break
        
        return count