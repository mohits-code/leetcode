class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=len(num)
        for i in range(l):
            if num[l-i-1]=="0":
                num=num[:-1]
            else:
                return num
        return num
        