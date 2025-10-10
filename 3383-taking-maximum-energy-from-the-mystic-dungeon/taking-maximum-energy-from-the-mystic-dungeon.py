class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        l=len(energy)
        total=-float("inf")
        for i in range(l-1,-1,-1):
            if i+k<l:
                energy[i]+=energy[i+k]
            if energy[i]>total:
                total=energy[i]
        return total