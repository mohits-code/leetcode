class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counterDict=defaultdict(int)

        for num in nums:
            counterDict[num]+=1
        
        freqArr = sorted(counterDict.values(), key=counterDict.get, reverse=True)

        maxFreq=0
        countFreq=0

        for freq in counterDict.values():
            if freq>countFreq:
                countFreq=freq
                maxFreq=1
            elif freq==countFreq:
                maxFreq+=1
        
        return maxFreq * countFreq

        