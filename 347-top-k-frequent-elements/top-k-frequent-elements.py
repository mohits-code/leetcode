class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        return sorted(freq.keys(), key=lambda x:freq[x], reverse=True)[:k]
        