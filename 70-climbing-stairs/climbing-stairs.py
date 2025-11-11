class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def recur(n):
            if n<=3:
                return n
            else:
                if n in d:
                    return d[n]
                d[n-1]=recur(n-1)
                return d[n-1]+recur(n-2)

        return recur(n)