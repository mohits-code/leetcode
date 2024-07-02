class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            n=int(str(x*-1)[::-1])*-1
        else:
            n=int(str(x)[::-1])

        if n>2147483647 or n<-2147483648:
            return 0
        return n