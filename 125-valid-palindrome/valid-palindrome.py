class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        while left<right:
            l=s[left]
            r=s[right]
            if not l.isalnum():
                left+=1
                continue
            if not r.isalnum():
                right-=1
                continue
            if lower(l)!=lower(r):
                return False
            left+=1
            right-=1
        return True
