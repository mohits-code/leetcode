class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=-1 if x<0 else 1
        n=0
        x=abs(x)
        while x>0:
            n=n*10+x%10
            x=x//10

        n=n*s
        if n>2147483647 or n<-2147483648:
            return 0
        return n