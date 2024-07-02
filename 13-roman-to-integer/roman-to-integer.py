class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        l=len(s)
        for i, char in enumerate(s):
            c=d[char]
            if i+1<l and c< d[s[i+1]]:
                total-=c
            else: 
                total+=c

        return total