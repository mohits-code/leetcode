class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=""
        arr = [str(i) for i in range(1, n + 1)]
        while arr:
            f=math.factorial(n)
            x=f/n
            y=int(math.ceil(float(k)/x))-1
            s+=arr[y]
            arr.pop(y)
            k=k%x
            n-=1
        return s

