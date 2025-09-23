class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")

        n=len(v1)
        m=len(v2)

        low=min(n,m)

        for i in range(low):
            num1=int(v1[i])
            num2=int(v2[i])
            if num1>num2:
                return 1
            elif num1<num2:
                return -1
        
        if low==n:
            for j in range(n,m):
                if int(v2[j])!=0:
                    return -1
        elif low==m:
            for h in range(m,n):
                if int(v1[h])!=0:
                    return 1
        
        return 0