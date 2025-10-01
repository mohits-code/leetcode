class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=0
        full=numBottles
        empty=0

        while not (full==0 and empty<numExchange):
            total+=full
            empty+=full

            full=empty//numExchange
            empty%=numExchange
            
        return total
