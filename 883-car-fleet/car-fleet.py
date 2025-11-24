class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=sorted(zip(position,speed))
        total=0
        curr=0
        for p,s in pair[::-1]:
            if (target-p)/s>curr:
                total+=1
                curr=(target-p)/s
        return total