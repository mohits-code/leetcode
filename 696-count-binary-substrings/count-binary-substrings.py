class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total=0
        curr=1
        prev=0
        l=len(s)

        for i in range(1,l):
            if s[i]!=s[i-1]:
                total+=min(curr, prev)
                prev=curr
                curr=1
            else:
                curr+=1

        total+=min(curr, prev)

        return total