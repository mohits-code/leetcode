class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=defaultdict(int)
        for num in arr1:
            d[num]+=1
        res=[]
        for num in arr2:
            res+=[num]*d[num]
            del d[num]
        
        for k in sorted(d):
            res+=[k]*d[k]

        return res