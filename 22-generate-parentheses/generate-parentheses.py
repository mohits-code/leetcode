class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def rec(x,curr,op):
            if x==0 and op==0:
                res.append(curr)
            if op>0:
                rec(x, curr+")", op-1)
            if x>0:
                rec(x-1, curr+"(", op+1)

        rec(n,"",0)
        return res