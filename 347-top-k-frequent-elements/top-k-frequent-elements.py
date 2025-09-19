class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= defaultdict(int)

        for num in nums:
            d[num]+=1
        
        return sorted(d, key=lambda x : d[x], reverse=True)[:k]