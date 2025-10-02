class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total=0

        for c in customers:
            if c=="Y":
                total+=1
            
        idx=-1
        count=total
        for i in range(len(customers)):
            if customers[i]=="Y":
                count-=1
                if count<total:
                    total=count
                    idx=i
            else:
                count+=1

        return idx+1