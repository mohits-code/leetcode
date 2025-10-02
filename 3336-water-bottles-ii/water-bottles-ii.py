class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange: return numBottles
        b=2*numExchange-3
        c=-2*numBottles
        cost = int((-1*b +  math.sqrt(b**2 - 4*c))-0.000000001)//2
        return numBottles+cost