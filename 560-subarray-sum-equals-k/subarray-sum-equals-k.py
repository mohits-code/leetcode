class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """



        prefixes=defaultdict(int)
        prefix=0
        counter=0
        prefixes[0]+=1

        for num in nums:
            prefix+=num            
            if prefix-k in prefixes:
                counter+=prefixes[prefix-k]
            prefixes[prefix]+=1


        return counter
