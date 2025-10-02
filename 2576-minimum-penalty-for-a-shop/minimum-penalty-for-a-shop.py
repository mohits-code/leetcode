class Solution:
    def bestClosingTime(self, customers: str) -> int:
        idx=0
        total=0
        curr=0
        for i in range(len(customers)):
            if customers[i]=="Y":
                curr-=1
                if curr<total:
                    total=curr
                    idx=i+1
            else:
                curr+=1

        return idx