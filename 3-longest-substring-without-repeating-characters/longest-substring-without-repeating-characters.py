class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        l=len(s)

        if l==1:
            return 1

        for i in range(l):
            arr=[]
            for j in range(i, l):
                if s[j] in arr:
                    break
                arr.append(s[j])
            count=max(count,len(arr))

        return count


        