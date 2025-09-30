class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        l=len(weights)
        if l<=k or k<2:
            return 0
        arr=[]
        for i in range(l-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        return sum(arr[-k+1:])-sum(arr[:k-1])

