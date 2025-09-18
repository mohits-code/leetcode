class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profits=[]

        globalMin=10001
        localMax=-1

        for price in prices:
            if price<globalMin:
                globalMin=price
                localMax=0
            if price>localMax:
                localMax=price
                profits.append(localMax-globalMin)

        return max(profits)