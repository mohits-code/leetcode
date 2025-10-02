class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total=0
        emptyBottles=0

        while numBottles !=0 or emptyBottles>numExchange:
            total+=numBottles
            emptyBottles+=numBottles
            numBottles=0
            while emptyBottles>=numExchange:
                numBottles+=1
                emptyBottles-=numExchange
                numExchange+=1

        return total