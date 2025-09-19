from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        answer=[0]*l
        stack=[]

        for i in range(l):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                answer[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        
        return answer


        