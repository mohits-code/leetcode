class Solution(object):
    def makeSmallestPalindrome(self, s):
        l=len(s)
        s=list(s)
        for i in range(l//2):
            j=l-i-1
            if s[i]>s[j]:
                s[i]=s[j]
            else:
                s[j]=s[i]
        return "".join(s)


        

        