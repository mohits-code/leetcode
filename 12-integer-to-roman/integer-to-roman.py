class Solution(object):
    def intToRoman(self, num):
        s=""
        d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        x=1
        while num>0:
            n=num%10
            if n==4:
                s=d[x]+d[x*5]+s
            elif n==9:
                s=d[x]+d[x*10]+s
            else:
                if n>=5:
                    n-=5
                    s=d[x]*n+s
                    s=d[x*5]+s
                else:
                    s=d[x]*n+s
            x*=10
            num//=10
        return s

                    


        
