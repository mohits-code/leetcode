class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        cost=prices[0]+prices[1]
        if money-cost<0:
            return money
        return money-cost
        