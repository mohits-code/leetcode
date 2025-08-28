class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        chars=defaultdict(int)
        for i in range(len(s)):
            chars[s[i]]+=1
            chars[t[i]]-=1
        for c in chars.values():
            if c!=0:
                return False
        return True

        