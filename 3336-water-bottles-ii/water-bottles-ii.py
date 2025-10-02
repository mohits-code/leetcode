class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange: return numBottles
        return numBottles + int(((-2*numExchange + 3) + math.sqrt((2*numExchange - 3)**2 - 4*-2*numBottles)) - 0.000000001)//2